import git

'''
    Given a path from the root of the current repo, returns the absolute path
'''
def abs_path(repo_path):
    repo = git.Repo('.', search_parent_directories=True)
    return repo.working_tree_dir + repo_path
