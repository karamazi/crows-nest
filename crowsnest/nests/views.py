from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Cluster
from .modelforms import ClusterForm

def index(request):
    clusters = Cluster.objects.order_by('id')
    view_vars = {
        "clusters": clusters
    }
    return render(request, 'index.html', view_vars)


def cluster_details(request, cluster_id):
    cluster = get_object_or_404(Cluster, pk=cluster_id)
    view_vars = {
        "cluster": cluster
    }
    return render(request, 'details.html', view_vars)


def add_cluster(request):
    if request.method == "POST":
        cluster_form = ClusterForm(request.POST)
        if cluster_form.is_valid():
            cluster_form.save()
            return HttpResponseRedirect('/')
    else:
        cluster_form = ClusterForm()

    return render(request, 'add_cluster.html', {'form': cluster_form})
