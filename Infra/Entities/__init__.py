from sqlalchemy.orm import declarative_base  # Alteração na importação

Base = declarative_base()


from .Ger_Time import *
from .Ger_Usuarios import *
from .Prc_Analise_Custos import *
from .Prc_Ativ_Cad import *
from .Prc_Auditoria import *
from .Prc_Cad import *
from .Prc_Capac_Operac import *
from .Prc_Compliance import *
from .Prc_Conhec import *
from .Prc_Entrega_Cli import *
from .Prc_Estr_Fisica import *
from .Prc_Estr_Logica import *
from .Prc_Forn_e_Itens_Cons import *
from .Ger_Indic import *
from .Prc_Modelagem import *
from .Prc_Rotina import *
from .Prj_Gestao import *
# Importe outros modelos conforme necessário

