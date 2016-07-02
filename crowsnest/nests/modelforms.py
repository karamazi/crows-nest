from django.forms import ModelForm
from nests.models import Cluster


class ClusterForm(ModelForm):
    class Meta:
        model = Cluster
        fields = '__all__'
