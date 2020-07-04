from gitlab_helper.AccessControlHelper import AccessControlHelper
import argparse

PARSER = argparse.ArgumentParser(description="Conceder acesso full aos repositórios do Gitlab")
PARSER.add_argument('--url', type=str, help="URL do Gitlab")
PARSER.add_argument('--token', type=str, help="Token de acesso ao Gitlab")
PARSER.add_argument('--userGroupId', type=int, help="ID do grupo de usuários")
PARSER.add_argument('--nivelAcesso', type=int, help="Nível de acesso a ser concedido")
PARSER.add_argument('--verbose', type=bool, default=False, help="Nível de verbosidade do log")
ARGS = PARSER.parse_args()

if ARGS.url is None:
    raise Exception("URL não informada.")
if ARGS.token is None:
    raise Exception("Token de acesso não informado.")
if ARGS.userGroupId is None:
    raise Exception("ID do grupo de usuários não informado.")
if ARGS.nivelAcesso is None:
    raise Exception("Nivel de acesso não informado.")

GitlabAccessControlHelper = AccessControlHelper(ARGS.url, ARGS.token)
GitlabAccessControlHelper.concederAcessoTodosRepositorios(ARGS.userGroupId, ARGS.nivelAcesso, ARGS.verbose)
