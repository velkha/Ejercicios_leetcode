/* NOTA PERSONAL - EN LOS EJERCICIOS DE LINKED LIST NO TIENES QUE CREARLA TU, LAS CLASES YA ESTAN CREADAS
FUERA DE LA FUNCION Y TU SOLO TIENES QUE USARLAS AUNQUE NO SE VEAN*/
function reverseList66(head: ListNode | null): ListNode | null {
    let prev = null

    while (head) {
        prev = new ListNode(head.val, prev)
        head = head.next
    }

    return prev
};

function reverseList55(head: ListNode | null): ListNode | null {
    let prev: ListNode | null = null;
    let current = head;
    let next: ListNode | null = null;

    while (current !== null) {
        next = current.next;  
        current.next = prev;  
        prev = current;      
        current = next;
    }
    return prev;
};

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */