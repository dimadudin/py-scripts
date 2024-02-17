def list_files(current_node, current_path=""):
    paths = []
    for parent, child in current_node.items():
        if child == None:
            paths.append(current_path + "/" + parent)
        else:
            paths.extend(list_files(child, current_path + "/" + parent))
    return paths

