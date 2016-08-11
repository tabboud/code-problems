#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0
#define MAX_DEPTH 10
#define MAX_CHILDREN 5

typedef struct data_ {
  int value;
  struct data_ **children;
} data_el;


int path_cnt=0;

void create_tree(data_el **);
int common_ancestor(data_el *, int, int);
int find_node(data_el *, data_el **, int);
void print_tree(data_el *);


int main(int argc, char **argv) {
  int value, i;
  data_el *tree;

  tree = NULL;

  create_tree(&tree);
  // print_tree(tree);

    common_ancestor(tree, atoi(argv[1]), atoi(argv[2]));
}


void create_tree(data_el **tree) {
    data_el *node1 = (data_el *)malloc(sizeof(data_el));
    data_el *node2 = (data_el *)malloc(sizeof(data_el));
    data_el *node3 = (data_el *)malloc(sizeof(data_el));
    data_el *node4 = (data_el *)malloc(sizeof(data_el));
    data_el *node5 = (data_el *)malloc(sizeof(data_el));
    data_el *node6 = (data_el *)malloc(sizeof(data_el));
    data_el *node7 = (data_el *)malloc(sizeof(data_el));
    data_el *node8 = (data_el *)malloc(sizeof(data_el));
    data_el *node9 = (data_el *)malloc(sizeof(data_el));
    data_el *node10 = (data_el *)malloc(sizeof(data_el));
    data_el *node11 = (data_el *)malloc(sizeof(data_el));
    data_el *node12 = (data_el *)malloc(sizeof(data_el));
    data_el *node13 = (data_el *)malloc(sizeof(data_el));
    data_el *node14 = (data_el *)malloc(sizeof(data_el));
    data_el *node15 = (data_el *)malloc(sizeof(data_el));
    data_el *node16 = (data_el *)malloc(sizeof(data_el));
    data_el *node17 = (data_el *)malloc(sizeof(data_el));

    node1->value = 7;
    node2->value = 3;
    node3->value = 9;
    node4->value = 11;
    node5->value = 10;
    node6->value = 8;
    node7->value = 6;
    node8->value = 2;
    node9->value = 12;
    node10->value = 4;
    node11->value = 5;
    node12->value = 1;
    node13->value = 13;
    node14->value = 14;
    node15->value = 15;
    node16->value = 16;
    node17->value = 17;

    // Add the children
    node1->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node2->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node3->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node4->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node5->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node6->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node7->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node8->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node9->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node10->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node11->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node12->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node13->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node14->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node15->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node16->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);
    node17->children = (data_el **)malloc(sizeof(data_el *)*MAX_CHILDREN);

    // NULL children nodes
    node4->children[0] = NULL;
    node5->children[0] = NULL;
    node7->children[0] = NULL;
    node8->children[0] = NULL;
    node9->children[0] = NULL;
    node11->children[0] = NULL;
    node12->children[0] = NULL;
    node14->children[0] = NULL;
    node15->children[0] = NULL;
    node16->children[0] = NULL;
    node17->children[0] = NULL;

    // Assign the child nodes
    node1->children[0] = node2;
    node1->children[1] = node9;
    node1->children[2] = node10;
    node1->children[3] = NULL;

    node2->children[0] = node3;
    node2->children[1] = node5;
    node2->children[2] = node6;
    node2->children[3] = NULL;

    node3->children[0] = node4;
    node3->children[1] = NULL;

    node6->children[0] = node7;
    node6->children[1] = node8;
    node6->children[2] = NULL;

    node10->children[0] = node11;
    node10->children[1] = node12;
    node10->children[2] = node13;
    node10->children[3] = NULL;

    node13->children[0] = node14;
    node13->children[1] = node15;
    node13->children[2] = node16;
    node13->children[3] = node17;
    node13->children[4] = NULL;

    *tree = node1;
}

void print_tree(data_el *root) {
    // base case
    if (root == NULL) {
        return; 
    }
    printf("val = %d\n", root->value);
    // Visit all of the children
    int i = 0;
    while (root->children[i] != NULL) {
        print_tree(root->children[i++]);
    }
}

int common_ancestor(data_el *root, int x, int y) {
    // Hold the addresses of every node on the path to node1 and node2
    data_el **node1_path = (data_el **)malloc(sizeof(data_el *)*MAX_DEPTH);
    data_el **node2_path = (data_el **)malloc(sizeof(data_el *)*MAX_DEPTH);

    // Find the paths
    if (find_node(root, node1_path, x) != TRUE) {
        printf("Node1 was not found in the tree\n");
        return FALSE;
    }
    path_cnt = 0;
            
    if (find_node(root, node2_path, y) != TRUE) {
        printf("Node2 was not found in the tree\n");
        return FALSE;
    }

    // Found the nodes, so compare the paths
    int i = 0;
    while (node1_path[i] == node2_path[i]){
        i++;
    }
    printf("common ancestor: %d\n", (node1_path[i-1])->value);
    return TRUE;
}

int find_node(data_el *root, data_el **path, int val) {
    // base case
    if (root == NULL) {
        return FALSE;
    }

    // store the address of the root into the path
    path[path_cnt++] = root;
    //printf("val=%d, i=%d\n", root->value, path_cnt);
    
    if (root->value == val) {
        //printf("Found the matching value!\n");
        return TRUE;
    }

    // Go through all children nodes
    int i = 0;
    while (root->children[i] != NULL) {
        if (find_node(root->children[i++], path, val)) {
            return TRUE;
        }
    }
    /*
    if ( (root->left && find_node(root->left, path, val)) || (root->right && find_node(root->right, path, val))) {
        return TRUE;
    }*/

    path_cnt--;
    return FALSE;
}

