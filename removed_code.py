"""
def project_created(sender, instance, created, **kwargs):
    if instance.status == 'Started processing.':
        return 
    else:
        project = NewProject.objects.get(id=instance.id)
        url_list = []
        if project.fastq_file1:
            if project.fastq_file2:
                url_list = [project.fastq_file1, project.fastq_file2]
            else:
                url_list = [project.fastq_file1]
        elif project.vcf_file1:
            url_list = [project.vcf_file1,]
        if url_list: 
            result = get_ftp_files.apply_async(args=[project.id, url_list,])
            if result.ready():
                print 'pasdf'
                instance.status = 'Started processing.'
                instance.save() 

""" 

# home/accounts/views.py
"""
class SignupView(View):
    form_class = UserProfileForm 
    second_form_class = UserForm 

    def get(self, request):
        user_form = UserProfileForm()
        user_profile_form = UserForm 
        return render(request, 'accounts/signup.html', {'user_form': user_form, 'user_profile_form': user_profile_form},)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home_page'))
        return render('accounts/signup.html', {'form': form},)



def signin(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('projects.views.dashboard'))
        else:
            return HttpResponseRedirect(reverse('accounts.views.disabled'))
    else:
        return HttpResponseRedirect(reverse('accounts.views.invalid'))


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm
        profile_form = UserProfileForm

    return render_to_response(
            'accounts/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered },
            context)

            
def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse('/rango/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details."
            return HttpResponse("Invaled details.")
    else:
        return render_to_response('rango/login.html', context)



def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('rango/login.html', {}, context)

"""

