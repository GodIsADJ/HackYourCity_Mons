from notable_trees import get_notable_trees, get_unique_list


if __name__ == "__main__":
    df_trees = get_notable_trees()
    tree_coord_list = get_unique_list(df_trees)
    print(tree_coord_list)