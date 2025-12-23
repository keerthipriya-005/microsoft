phone_book={}
def add_contact():
    name=input("enter  the name:").strip().lower()
    phone_num=int(input("enter the phone num:"))
    phone_book[name]=phone_num
    print("-------contact saved successfully--------")
def read_contact():
    search_name=input("enter the searching name").strip().lower()
    if search_name in phone_book.keys():
       print()
       print('----------------------')
       print(f"the number for{search_name.capitalize()} is:{phone_book}")
    else:
        print("contact is not invalide") 
def update_contact():
    update_name = input("enter the name").strip().lower()
    update_number = int(input("enterr the new number to update:"))
    phone_book[update_name] = update_number
def main():
     while(True):
        print()
        print("choose the task from the below option")
        print("""
                1. add contact
                2.read contact
                3.update contact
                4. delete contact""")
        choice = int(input("enter the choice"))
        if choice ==1:
             add_contact()
        elif choice == 2:
             read_contact()
        elif choice == 3:
            update_contact()
        else:
           break
if_name_ ='_main_'
main()
