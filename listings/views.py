def new_listing(request):
    if request.method != 'POST':
        form = ListingForm()
    else:
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings:all_listings')
      
    context = {'form': form}
    return render(request, 'listings/new_listing.html', context)
