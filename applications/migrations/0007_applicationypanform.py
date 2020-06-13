# Generated by Django 3.0.4 on 2020-06-11 20:05

import applications.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0006_auto_20200528_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationYpanForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Σε εκκρεμότητα', 'Σε εκκρεμότητα'), ('Απορρίφθηκε', 'Απορρίφθηκε'), ('Εγκρίθηκε', 'Εγκρίθηκε')], default='Σε εκκρεμότητα', max_length=30, verbose_name='Κατασταση')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Ημ/νία υποβολής')),
                ('Activity_Field_App', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Αίτηση με ακριβή αναφορά του πεδίου δραστηριοποίησης')),
                ('Cert_ID', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό Διαπίστευσης ΕΣΥΔ με παραρτήματα')),
                ('Non_Bankruptcy_Cert_1', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό Πρωτοδικείου περί μη πτώχευσης σε ισχύ')),
                ('Non_Bankruptcy_Cert_2', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό Πρωτοδικείου περί μη κατάθεσης αίτησης πτωχεύσεως σε ισχύ')),
                ('Non_Clearance_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε εκκαθάριση σε ισχύ')),
                ('Non_Force_Arrange_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε αναγκαστική διαχείριση σε ισχύ')),
                ('GEMI_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Πιστοποιητικό ΓΕΜΗ Γενικής Χρήσης και Εκπροσώπησης')),
                ('Tax_Clear_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Αποδεικτικό ενημερότητας για χρέη προς το Δημόσιο')),
                ('Insurance_Liability_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Βεβαίωση ΙΚΑ περί ασφαλιστικής ενημερότητας σε ισχύ')),
                ('Civil_ID', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Βεβαίωση ασφάλισης επαγγελματικής αστικής ευθύνης για την κάλυψη κινδύνων των παρεχόμενων υπηρεσιών')),
                ('Balance_Sheet_3Y', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Ισολογισμοί τριών τελευταίων ετών')),
                ('Art_Of_Incorporation', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Κωδικοποιημένο καταστατικό της εταιρείας')),
                ('GEMI_NoMod_Cert', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Βεβαίωση περί μη τροποποίησης του πιστοποιητικού ΓΕΜΗ')),
                ('Foreign_Activity_Decl', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Υπεύθυνη δήλωση του κοινοποιημένου οργανισμού για τη δραστηριοποίησή του ή μη σε άλλες χώρες')),
                ('Coord_Group_Decl', models.FileField(upload_to=applications.models.generate_filename_ypan, verbose_name='Υπεύθυνη δήλωση του κοινοποιημένου φορέα για τη συμμετοχή του ή μη στις ομάδες συντονισμού')),
                ('esyd_app', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ypan_app', to='applications.ApplicationForm')),
                ('foreas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]