from gitlab_helper.CloneSyncHelper import CloneSyncHelper
import argparse

PARSER = argparse.ArgumentParser(description="Clonar ou atualizar grupo de repositorios")
PARSER.add_argument('--url', type=str, help="URL do Gitlab")
PARSER.add_argument('--token', type=str, help="Token de acesso ao Gitlab")
PARSER.add_argument('--userGroupId', type=int, help="ID do grupo de usuários")
PARSER.add_argument('--basePath', type=str, help="Path base para os repositorios")
ARGS = PARSER.parse_args()

if ARGS.url is None:
    raise Exception("URL não informada.")
if ARGS.token is None:
    raise Exception("Token de acesso não informado.")
if ARGS.userGroupId is None:
    raise Exception("ID do grupo de usuários não informado.")
if ARGS.basePath is None:
    raise Exception("Path base para o clone não informado.")

GitlabCloneSyncHelper = CloneSyncHelper(ARGS.url, ARGS.token)
GitlabCloneSyncHelper.cloneUpdateGroup(ARGS.userGroupId, ARGS.basePath)
