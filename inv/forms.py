from django import forms

from inv.models import Categoria, SubCategoria, Marca, UniMedida


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        widget = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(estado=True).order_by('descripcion'))
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        widget = {
            'descripcion': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = 'Seleccione Categoría'

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la marca',
                  'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class UniMedidaForm(forms.ModelForm):
    class Meta:
        model = UniMedida
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la unidad de medida',
                  'estado': 'Estado'}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })