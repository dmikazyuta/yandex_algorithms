"""

ID: 69973935

Алгоритм:

Разобьем решение на 2 шага:
1. Поиск узла для удаления -- search_node_by_key
Реализуем через while. Двигаемся по дереву, используя свойства BST
После нахождения узла передаем его в функцию удаления. Повторных обходов не происходит, рассматривается поддерево.
2. Поиск узла для замены удаляемого + действие по удалению -- remove_node
Для реализации поиска и восстановления целостности обработаем все варианты положения узла.
Подробнее отразил в комментариях, в самой функции.
Для обхода дерева выбирается поиск минимума в правом поддереве.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(h), где h — высота дерева

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Общая сложность - O(n), где n - кол-во узлов дерева
Поскольку поиск осуществляется без дополнительных структур памяти

"""

def remove_node(node, parent, root):

    # Нет потомков
    if node.left is None and node.right is None:
        # Нет потомков, есть родитель
        if parent is not None:
            # Для родителя это левый потомок
            if parent.left == node:
                parent.left = None
            # Для родителя это правый потомок
            else:
                parent.right = None
            return root
        # Нет потомков, нет родителей
        else:
            return None

    # Есть потомок справа
    if node.left is None:
        new_node = node.right
        # Есть потомок справа, есть родитель
        if parent is not None:
            node.right = new_node.right
            node.value = new_node.value
            return root
        # Есть потомок справа, нет родителя
        else:
            return new_node

        #return parent

    # Есть потомок слева
    if node.right is None:
        new_node = node.left
        # Есть потомок слева, есть родитель
        if parent is not None:
            node.left = new_node.left
            node.value = new_node.value
            return root
        # Есть потомок слева, нет родителя
        else:
            return new_node
        #return parent

    # Ищем минимальный элемент справа

    new_parent = node
    new_node = node.right

    while new_node.left is not None:
        new_parent = new_node
        new_node = new_node.left

    if new_parent != node:
        new_parent.left = new_node.right
    else:
        new_parent.right = new_node.right

    node.value = new_node.value

    return root


def search_node_by_key(root, key):
    if root is None:
        return None

    prev_parent = None
    node = root

    while node is not None:
        parent = node
        if key > parent.value:
            node = parent.right
            prev_parent = parent
        elif key < parent.value:
            node = parent.left
            prev_parent = parent
        else:
            return remove_node(node, prev_parent, root)

    return root


def remove(root, key):
    return search_node_by_key(root, key)