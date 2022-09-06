from django.shortcuts import render , redirect
from app.models import File , Folder
from app.forms import CustomerRegistrationForm
from django.views import View
from django.contrib import messages
from app.forms import ImageForm , FolderName
from django.contrib.auth import logout

# Create your views here.

def uploadFile(request):
    if request.method == 'POST':
        img = request.POST['file']
        name = request.POST['name']
        id = Folder.objects.get(user=request.user,name='test3')

        if img:
            f = File(name=name,user=request.user,folder=id.id,description=None,location=img)
            f.save()
            print("---------------------------------------------------------------")

    return redirect('drive')

def home(request):
    if request.user.is_authenticated:
        fileDe = Folder.objects.filter(user=request.user,folder=None) 
        print(fileDe)
        if 'fileupload' in request.method=='POST' :
            form = ImageForm(request.POST,request.FILES)
            if form.is_valid():
                img = form.cleaned_data['img']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                f = File(name=name,user=request.user,folder=id,description=description,location=img)
                f.save() 
            form = ImageForm()
            foldeform = FolderName()
        elif request.method == 'POST':
            foldeform = FolderName(request.POST)
            if foldeform.is_valid():
                fn = foldeform.cleaned_data['fname']
                f = Folder(user=request.user,folder=None,name=fn)
                f.save()
        form = ImageForm()
        foldeform = FolderName()
        return render(request,'file.html',{'fm':form,'foldeform':foldeform,'fileAll':fileDe})
    else:
        return redirect("login")


def inside(request,name):
    if request.user.is_authenticated:
        id = Folder.objects.get(user=request.user,name=name)
        fileDe = Folder.objects.filter(user=request.user,folder=id.id)
        data = File.objects.filter(user=request.user,folder=id.id)
        bottomwears = File.objects.filter(user=request.user,folder=id.id)
        if 'fileupload' in request.POST:
            if request.method=='POST':
                
                form = ImageForm(request.POST,request.FILES)
                if form.is_valid():
                    img = form.cleaned_data['img']
                    name = form.cleaned_data['name']
                    description = form.cleaned_data['description']
                    f = File(name=name,user=request.user,folder=id,description=description,location=img)
                    f.save()
                    print("successfully")
        if 'foldercreate' in request.POST:
            if request.method=='POST':
                foldeform = FolderName(request.POST)
                print(foldeform)
                if foldeform.is_valid():
                    fn = foldeform.cleaned_data['fname']
                    print(fn)
                    f = Folder(user=request.user,folder=id,name=fn)
                    print(f)
                    f.save()
        form = ImageForm()
        foldeform = FolderName()
        return render(request,'file.html',{'fileAll':fileDe,'foldeform':foldeform,'data':data,'fm':form})
    else:
        return redirect('login')

def twoinside(request,name1 , name2):
    if request.user.is_authenticated:
        id = Folder.objects.get(user=request.user,name=name2)
        fileDe = Folder.objects.filter(user=request.user,folder=id.id) 
        data = File.objects.filter(user=request.user,folder=id.id)
        if 'fileupload' in request.POST:
            if request.method=='POST':
                form = ImageForm(request.POST,request.FILES)
                if form.is_valid():
                    img = form.cleaned_data['img']
                    name = form.cleaned_data['name']
                    description = form.cleaned_data['description']
                    f = File(name=name,user=request.user,folder=id,description=description,location=img)
                    f.save()
                    print("successfully")
        if 'foldercreate' in request.POST:
            if request.method == 'POST':
                foldeform = FolderName(request.POST)
                print(foldeform)
                if foldeform.is_valid():
                    fn = foldeform.cleaned_data['fname']
                    print(fn)
                    f = Folder(user=request.user,folder=id,name=fn)
                    print(f)
                    f.save()
        form = ImageForm()
        foldeform = FolderName()
        return render(request,'file.html',{'fileAll':fileDe,'foldeform':foldeform,'data':data,'fm':form})
    else:
        return redirect('login')



class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'customerregistration.html', {'form':form})
  
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully.')
   form.save()
  else:
    messages.error(request, 'Sorray sometime wrong')
  return render(request, 'customerregistration.html', {'form':form})

def redirectview(request):
    return redirect('/')

def logout(request):
    logout(request)
    return redirect('login')