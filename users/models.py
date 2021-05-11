from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utils import validate_cpf

class MyUserModel(AbstractUser):
    name = models.CharField(
        verbose_name="nome", 
        max_length=50, 
        validators=[RegexValidator(regex='[0-9a-zA-Z]{3}[0-9a-zA-Z]*', 
            message='Nome deve conter apenas letras e números.', 
            code='erro')]
    )
    surname = models.CharField(
        verbose_name="sobrenome", 
        max_length=700, 
        validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', 
            message='Sobrenome deve conter apenas letras, números e espaços.', 
            code='erro')]
    )
    cpf = models.CharField(
        max_length=11, 
        help_text='Deverá conter apenas números', 
        unique=True, 
        validators=[validate_cpf],
        verbose_name="CPF"
    )
    adress = models.CharField(
        verbose_name="endereço", 
        max_length=50
    )
    number = models.CharField(
        verbose_name="número", 
        max_length=5, 
        validators=[RegexValidator(regex='[0-9]+', 
            message='Deve conter apenas números maiores que 0', 
            code='erro')]
    )
    complement = models.CharField(
        verbose_name="complemento", 
        max_length=30,
        blank=True
    )
    zip_code = models.CharField(
        verbose_name="CEP", 
        validators=[RegexValidator(regex='7[0-3][0-9]{3}-[0-9]{3}', 
        message='CEP deve estar no formato xxxxx-xxx, e ser um CEP do DF', 
            code='erro')],
            max_length=9
    )
    district = models.CharField(
        max_length=20, 
        verbose_name = "bairro", 
        choices=(
            ('aguas_claras', 'Águas Claras'),
            ('brazlandia', 'Brazlândia'),
            ('candangolandia', 'Candangolândia'),
            ('ceilandia', 'Ceilândia'),
            ('cruzeiro', 'Cruzeiro'),
            ('fercal', 'Fercal'),
            ('gama', 'Gama'),
            ('guara', 'Guará'),
            ('itapoa', 'Itapoã'),
            ('jardim_botanico', 'Jardim Botânico'),
            ('lago_norte', 'Lago Norte'),
            ('lago_Sul', 'Lago Sul'),
            ('nucleo_bandeirante', 'Núcleo Bandeirante'),
            ('paranoa', 'Paranoá'),
            ('park_way', 'Park Way'),
            ('planaltina', 'Planaltina'),
            ('plano_piloto', 'Plano Piloto'),
            ('samambaia', 'Samambaia'),
            ('taguatinga', 'Taguatinga'),
            ('recanto_das_emas', 'Recanto das Emas'),
            ('riacho_fundo_1', 'Riacho Fundo 1'),
            ('riacho _fundo_2', 'Riacho Fundo 2'),
            ('santa_maria', 'Santa Maria'),
            ('SCIA', 'SCIA'),
            ('SIA', 'SIA'),
            ('sao_sebastiao', 'São Sebastiao'),
            ('sobradinho', 'Sobradinho'),
            ('sobradinho_2', 'Sobradinho 2'),
            ('sudoeste', 'Sudoeste'),
            ('varjao', 'Varjão'),
            ('vicente pires', 'Vicente Pires'),)
    )

    state = models.CharField(
        verbose_name="estado",
        max_length=2,
        default='DF'
    )

    first_name = False
    last_name = False
    REQUIRED_FIELDS = []

