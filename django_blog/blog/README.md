#CRUD OPERATIONS:
inherit from base classes #from django.views.generics import ListView, DetailView, DeleteVied, UpdateView.
1.LIST VIEW:    1.specify model
                2.specify template name
                3.specify success |url if needed

2.DetailView;:this displays individual blog post.
                1.specify model
                2.specify template name: 
                3.SET , context_object_name = "post" this serves as reference name we use while rendering template we specified in template name. a html template uses the name to fetch data from the database.

3.createview: This view called when user want to create post.
                #form
            1.in form.py create a createpost form class that inherits from modelsForm.
            2.specify model to candle in form
            3.specify the fields you need.(in out case we needed title and content.)
                # back to the view
            4.specify model: in our case it is post
            5.specify formclass 
            6. specify success url.
            7. define form valid function: This is overriden if you want to define the custom behaviour. since oin our case , we need to set the author programatically , thats what we are doing to use it for.
            #def form_valid(self,form)
                #form.instance.author = self.request.user
                #return super().form_valid(form): this function saves the form to tha database and calls success url


4.updateview
5.deleteview


