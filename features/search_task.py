def search_task(tasks):
    if not tasks:
        print("Belum ada task yang tersedia.")
        return

    keyword = input("Masukkan nama assignee yang dicari: ").lower()
    found = False

    print(f"\nHasil pencarian untuk assignee '{keyword}':")
    for idx, task in enumerate(tasks):
        assignee_name = task.get('assignee', '').lower()
        if keyword in assignee_name:
            print(f"{idx + 1}. {task.get('task')} - {task.get('assignee')} [{task.get('status')}]")
            found = True
    
    if not found:
        print("Tidak ada task yang ditemukan untuk assignee tersebut.")
