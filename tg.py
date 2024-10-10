from tabulate import tabulate

class Telegram:
    def __init__(self, user_name):
        self.user_name = user_name
        self.inbox = []  
        self.sent_messages = []
    
    def send(self, recipient, message):
        xabar = {
            'sender': self.user_name,
            'text': message,
            'status': 'sending',
            'time': self.get_time()
        }
        recipient.inbox.append(xabar) 
        self.sent_messages.append(xabar) 
        print(f"{self.user_name} '{recipient.user_name}' foydalanuvchisiga xabar yubordi: '{message}'")
    
    def read(self):
        if not self.inbox:
            print(f"{self.user_name}da yangi xabar yo'q.")
            return
        
        print(f"{self.user_name}ning olingan xabarlari:")
        rows = []
        for idx, xabar in enumerate(self.inbox, 1):
            rows.append([idx, xabar['text'], xabar['sender'], xabar['status'], xabar['time']])
            xabar['status'] = 'reading'
        
        print(tabulate(rows, headers=["#", "Text", "Sender", "Status", "Time"], tablefmt="grid"))
    
    def delete(self, index):
        if 0 < index <= len(self.inbox):
            deleted_message = self.inbox.pop(index - 1)
            print(f"{self.user_name} '{deleted_message['text']}' xabarini o'chirdi.")
        else:
            print(f"Xato: Xabar topilmadi.")
    
    def get_time(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

user1 = Telegram("User1")
user2 = Telegram("User2")

user1.send(user2, "Qondaye, User2!")
user2.read()

user2.delete(1)

user1.send(user2, "Yaxshimi?")
user2.read()

print(f"\n{user1.user_name}ning yuborgan xabarlari:")
rows = []
for xabar in user1.sent_messages:
    rows.append([xabar['text'], xabar['status'], xabar['time']])

print(tabulate(rows, headers=["Text", "Status", "Time"], tablefmt="grid"))
