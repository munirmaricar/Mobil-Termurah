from django import forms

from tugas.models import Porto

class Portofield(forms.ModelForm):
    class Meta:
        model = Porto
        fields = ("judulproyek","tanggalmulai","tanggalselesai","deskripsi","tempat","kategori")
        labels = {
            "judulproyek":"Judul Proyek",
            "tanggalmulai":"Tanggal Mulai yyyy-mm-dd",
            "tanggalselesai":"Tanggal Selesai yyyy-mm-dd",
            "deskripsi":"Deskripsi",
            "tempat":"Tempat",
            "kategori":"Kategori"
        }