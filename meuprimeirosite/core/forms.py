from django import forms
from django.core.mail.message import EmailMessage


class FormContato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150)
    email = forms.EmailField(label='E-mail', max_length=150)
    telefone = forms.CharField(label='Telefone', max_length=20)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'De: {nome}\n' \
                   f'{mensagem}\n'  \
                    f'{telefone}'
        mail = EmailMessage(
            subject=f'contato de: {nome}',
            body=conteudo,
            from_email= 'contato@minhaempresa.com',
            to=['contato@minhaempresa.com',],
            headers={'Replay-To': email}
        )
        mail.send()