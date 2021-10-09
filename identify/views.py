from django.shortcuts import render

# Create your views here.
from django.views import View

from api.models import Function, Category, SubCategory, Level, Option


class Identify(View):

    @staticmethod
    def get(request, category_id=None, subcategory_id=None, level_id=None):
        # if category_id == 0 or subcategory_id == 0 or level_id == 0:
        #     print("ddd")
        #     category_id = 1
        #     subcategory_id = 1
        #     level_id = 1
        function = Function.objects.all()
        # category = Category.objects.filter(function_id=1)
        # sub_category = SubCategory.objects.get(id=subcategory_id, category_id=category_id)
        # level = Level.objects.get(id=level_id)
        # options = Option.objects.filter(level_id=level_id)
        # if Level.objects.filter(id=level_id + 1).exists():
        #     nextitem = {'next_sub': subcategory_id, 'next_level': level_id + 1}
        #     # preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        # else:
        #     print(sub_category)
        #     nextitem = {'next_sub': subcategory_id + 1, 'next_level': 1}
        #     # preitem = {'pre_sub': subcategory_id - 1, 'pre_level': 1}
        #
        # if Level.objects.filter(id=level_id - 1).exists():
        #     preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        # else:
        #     latestid = Level.objects.latest('id').id
        #     preitem = {'pre_sub': subcategory_id - 1, 'pre_level': latestid}
        #
        # context = {'function': function,
        #            'active': 1,
        #            'progressbars': category,
        #            'subcat': sub_category,
        #            'question': sub_category.subcategory_details,
        #            'level': level,
        #            'options': options,
        #            'next': nextitem,
        #            'pre': preitem,
        #             'funname':'IDENTIFY (ID)'
        #            }

        return render(request, 'identify.html',{'function': function,'active':1})


class Protect(View):

    @staticmethod
    def get(request,category_id=None, subcategory_id=None, level_id=None):
        # if category_id == 0 or subcategory_id == 0 or level_id == 0:
        #     print("ddd")
        #     category_id = 1
        #     subcategory_id = 1
        #     level_id = 1
        function = Function.objects.all()
        # category = Category.objects.filter(function_id=2)
        # sub_category = SubCategory.objects.get(id=subcategory_id, category_id=category_id)
        # level = Level.objects.get(id=level_id)
        # options = Option.objects.filter(level_id=level_id)
        # if Level.objects.filter(id=level_id + 1).exists():
        #     nextitem = {'next_sub': subcategory_id, 'next_level': level_id + 1}
        #     # preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        # else:
        #     print(sub_category)
        #     nextitem = {'next_sub': subcategory_id + 1, 'next_level': 1}
        #     # preitem = {'pre_sub': subcategory_id - 1, 'pre_level': 1}
        #
        # if Level.objects.filter(id=level_id - 1).exists():
        #     preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        # else:
        #     latestid = Level.objects.latest('id').id
        #     preitem = {'pre_sub': subcategory_id - 1, 'pre_level': latestid}
        #
        # context = {'function': function,
        #            'active': 1,
        #            'progressbars': category,
        #            'subcat': sub_category,
        #            'question': sub_category.subcategory_details,
        #            'level': level,
        #            'options': options,
        #            'next': nextitem,
        #            'pre': preitem,
        #            'funname': 'PROTECT (PR)'
        #            }

        return render(request, 'protect.html',{'function': function})



class Detect(View):

    @staticmethod
    def get(request, category_id, subcategory_id, level_id):
        if category_id == 0 or subcategory_id == 0 or level_id == 0:
            print("ddd")
            category_id = 1
            subcategory_id = 1
            level_id = 1
        function = Function.objects.all()
        category = Category.objects.filter(function_id=3)
        sub_category = SubCategory.objects.get(id=subcategory_id, category_id=category_id)
        level = Level.objects.get(id=level_id)
        options = Option.objects.filter(level_id=level_id)
        if Level.objects.filter(id=level_id + 1).exists():
            nextitem = {'next_sub': subcategory_id, 'next_level': level_id + 1}
            # preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            print(sub_category)
            nextitem = {'next_sub': subcategory_id + 1, 'next_level': 1}
            # preitem = {'pre_sub': subcategory_id - 1, 'pre_level': 1}

        if Level.objects.filter(id=level_id - 1).exists():
            preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            latestid = Level.objects.latest('id').id
            preitem = {'pre_sub': subcategory_id - 1, 'pre_level': latestid}

        context = {'function': function,
                   'active': 1,
                   'progressbars': category,
                   'subcat': sub_category,
                   'question': sub_category.subcategory_details,
                   'level': level,
                   'options': options,
                   'next': nextitem,
                   'pre': preitem,
                   'funname': 'DETECT (DE)'
                   }

        return render(request, 'identify.html', context)



class Respond(View):

    @staticmethod
    def get(request, category_id, subcategory_id, level_id):
        if category_id == 0 or subcategory_id == 0 or level_id == 0:
            print("ddd")
            category_id = 1
            subcategory_id = 1
            level_id = 1
        function = Function.objects.all()
        category = Category.objects.filter(function_id=4)
        sub_category = SubCategory.objects.get(id=subcategory_id, category_id=category_id)
        level = Level.objects.get(id=level_id)
        options = Option.objects.filter(level_id=level_id)
        if Level.objects.filter(id=level_id + 1).exists():
            nextitem = {'next_sub': subcategory_id, 'next_level': level_id + 1}
            # preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            print(sub_category)
            nextitem = {'next_sub': subcategory_id + 1, 'next_level': 1}
            # preitem = {'pre_sub': subcategory_id - 1, 'pre_level': 1}

        if Level.objects.filter(id=level_id - 1).exists():
            preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            latestid = Level.objects.latest('id').id
            preitem = {'pre_sub': subcategory_id - 1, 'pre_level': latestid}

        context = {'function': function,
                   'active': 1,
                   'progressbars': category,
                   'subcat': sub_category,
                   'question': sub_category.subcategory_details,
                   'level': level,
                   'options': options,
                   'next': nextitem,
                   'pre': preitem,
                   'funname': 'RESPOND (RS)'
                   }

        return render(request, 'identify.html', context)


class Recover(View):

    @staticmethod
    def get(request, category_id, subcategory_id, level_id):
        if category_id == 0 or subcategory_id == 0 or level_id == 0:
            print("ddd")
            category_id = 1
            subcategory_id = 1
            level_id = 1
        function = Function.objects.all()
        category = Category.objects.filter(function_id=5)
        sub_category = SubCategory.objects.get(id=subcategory_id, category_id=category_id)
        level = Level.objects.get(id=level_id)
        options = Option.objects.filter(level_id=level_id)
        if Level.objects.filter(id=level_id + 1).exists():
            nextitem = {'next_sub': subcategory_id, 'next_level': level_id + 1}
            # preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            print(sub_category)
            nextitem = {'next_sub': subcategory_id + 1, 'next_level': 1}
            # preitem = {'pre_sub': subcategory_id - 1, 'pre_level': 1}

        if Level.objects.filter(id=level_id - 1).exists():
            preitem = {'pre_sub': subcategory_id, 'pre_level': level_id - 1}
        else:
            latestid = Level.objects.latest('id').id
            preitem = {'pre_sub': subcategory_id - 1, 'pre_level': latestid}

        context = {'function': function,
                   'active': 1,
                   'progressbars': category,
                   'subcat': sub_category,
                   'question': sub_category.subcategory_details,
                   'level': level,
                   'options': options,
                   'next': nextitem,
                   'pre': preitem,
                   'funname': 'RECOVER (RC)'
                   }

        return render(request, 'identify.html', context)