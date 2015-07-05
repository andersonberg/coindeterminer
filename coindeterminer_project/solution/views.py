import os
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.conf import settings
from django.template import RequestContext
from .models import Coin, Solution
from .forms import InputForm

class HomeView(TemplateView):
    template_name = 'home.html'
    list_coins = []
    input_list = []
    form_class = InputForm

    def get(self, request, *args, **kwargs):
        self.input_list.clear()
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # get a document from form
            docfile = request.FILES['input_file']
            docpath = settings.SITE_ROOT + "/documents/"
            self.save_document(docfile, docpath)
            self.read_input(docpath, docfile)

        return render(request, self.template_name, {'form': form, 'inputs': self.input_list})

    def get_coins(self):
        """
        Get list of coins in database
        """
        coins = Coin.objects.get_all()
        for coin in coins:
            self.list_coins.append(coin.value)

    def coin_determiner(self, num):
        """
        Calculates the number of coins required to reach the amount provided
        :param num: amount
        :return: quantity of coins
        """
        current_coin = self.list_coins.pop()

        # get quotient and remainder of the division between the amount and current coin
        quotient = num//current_coin
        rest = num % current_coin

        # if the quotient is equals to 0 or the rest is different from 0, sums the current quotient
        # and the quotient of the division between the next coin available and the current rest
        # if not, returns the current quotient
        if quotient == 0 or (rest != 0 and len(self.list_coins) > 0):
            return quotient + self.coin_determiner(rest)
        else:
            return quotient

    def read_input(self, filepath, filename):
        """
        Reads the file with provided input
        :param filename: the file
        """
        filename = filepath + filename.name
        with open(filename, 'r') as file_input:
            for line in file_input.readlines():
                self.input_list.append(int(line))

    def get_solution(self, num):
        solutions = []
        for i in range(len(self.list_coins)):
            local_solution = self.coin_determiner(num)
            solutions.append(local_solution)

        return min(solutions)

    def save_document(self, docfile, docpath):
        """
        Saves the document
        :param docfile: filename
        :param docpath: absolute path
        """
        if not os.path.exists(docpath):
            os.makedirs(docpath)
        doc_fullpath = docpath + docfile.name
        with open(doc_fullpath, 'wb+') as document:
            for chunk in docfile.chunks():
                document.write(chunk)
