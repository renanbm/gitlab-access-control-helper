from gitlab_helper.AccessControlHelper import AccessControlHelper
import gitlab
import argparse

PARSER = argparse.ArgumentParser(description="Conceder acesso para uma lista de grupo de usuários em uma lista de repositórios do Gitlab")
PARSER.add_argument('--url', type=str, help="URL do Gitlab")
PARSER.add_argument('--token', type=str, help="Token de acesso ao Gitlab")
PARSER.add_argument('--userGroupIdList', type=int, nargs="*", help="Lista dos IDs dos grupos que serão relacionados ao repositório")
PARSER.add_argument('--projectIdList', type=int, nargs="*", help="Lista de IDs de repositórios")
PARSER.add_argument('--nivelAcesso', type=str, help="Nível de acesso a ser concedido")
PARSER.add_argument('--verbose', type=bool, default=False, help="Nível de verbosidade do log")
ARGS = PARSER.parse_args()

if ARGS.url is None:
    raise Exception("URL não informada.")
if ARGS.token is None:
    raise Exception("Token de acesso não informado.")
if ARGS.userGroupIdList is None:
    raise Exception("ID do grupo de usuários não informado.")
if ARGS.projectIdList is None:
    raise Exception("ID do grupo de projetos não informado.")
if ARGS.nivelAcesso is None:
    raise Exception("Nivel de acesso não informado.")

nivelAcesso = str()

if ARGS.nivelAcesso == "Guest":
    nivelAcesso = gitlab.GUEST_ACCESS
elif ARGS.nivelAcesso == "Reporter":
    nivelAcesso = gitlab.REPORTER_ACCESS
elif ARGS.nivelAcesso == "Developer":
    nivelAcesso = gitlab.DEVELOPER_ACCESS
elif ARGS.nivelAcesso == "Maintainer":
    nivelAcesso = gitlab.MAINTAINER_ACCESS

GitlabAccessControlHelper = AccessControlHelper(ARGS.url, ARGS.token)
for userGroupId in ARGS.userGroupIdList:
    for projectId in ARGS.projectIdList:
        GitlabAccessControlHelper.concederAcessoGrupoUsuariosRepositorio(projectId, userGroupId, nivelAcesso, ARGS.verbose)
