from instabot import Bot

# Botu oluştur
bot = Bot()

# Giriş yap
username = "kullanıcı adınız"
password = "şifreniz"
bot.login(username=username, password=password)

def show_help():
    print("""
    Komutlar:
    1. message @kullanici mesaj - Belirtilen kullanıcıya mesaj gönderir.
    2. message -r sayı @kullanici mesaj - Belirtilen kullanıcıya belirtilen sayıda mesaj gönderir.
    3. follow @kullanici - Belirtilen kullanıcıyı takip eder.
    4. unfollow @kullanici - Belirtilen kullanıcıyı takipten çıkarır.
    5. like @kullanici - Belirtilen kullanıcının son gönderisini beğenir.
    6. like_user @kullanici miktar - Belirtilen kullanıcının gönderilerini beğenir.
    7. comment @kullanici yorum - Belirtilen kullanıcının son gönderisine yorum yapar.
    8. get_followers - Hesabının takipçilerini listeler.
    9. get_following - Takip ettiğin kullanıcıları listeler.
    10. delete_last_comment - Son yaptığın yorumu siler.
    11. get_user_info @kullanici - Belirtilen kullanıcının bilgilerini gösterir.
    12. block @kullanici - Belirtilen kullanıcıyı engeller.
    13. unblock @kullanici - Belirtilen kullanıcının engelini kaldırır.
    14. send_story @kullanici - Belirtilen kullanıcıya hikaye gönderir.
    15. download_profile @kullanici - Belirtilen kullanıcının profil resmini indirir.
    16. get_user_media @kullanici - Belirtilen kullanıcının gönderilerini listeler.
    17. hashtag_search #hashtag - Belirtilen hashtag ile gönderileri arar.
    18. save_media @kullanici - Belirtilen kullanıcının gönderisini kaydeder.
    19. edit_caption @kullanici yeni_yazi - Belirtilen kullanıcının son gönderisinin açıklamasını değiştirir.
    20. get_media_comments @kullanici - Kullanıcının son gönderisine yapılan yorumları listeler.
    21. get_user_likes @kullanici - Kullanıcının beğendiği gönderileri listeler.
    22. mute @kullanici - Belirtilen kullanıcının bildirimlerini sessize alır.
    23. unmute @kullanici - Belirtilen kullanıcının bildirim sessizliğini kaldırır.
    24. share_post @kullanici - Kullanıcının son gönderisini paylaşır.
    25. send_location @kullanici konum - Belirtilen kullanıcıya konum gönderir.
    26. clear_chat @kullanici - Belirtilen kullanıcı ile yapılan sohbeti temizler.
    27. get_saved_media - Kaydedilmiş gönderileri listeler.
    28. view_story @kullanici - Kullanıcının hikayesini görüntüler.
    29. schedule_post @kullanici tarih mesaj - Belirtilen tarihte bir gönderi paylaşır.
    30. exit - Çıkış yapar.
    """)

while True:
    command = input("Komut girin (help için 'help' yazın): ").strip().lower()

    if command == "help":
        show_help()
    
    # Önceki komutlar burada...

    elif command.startswith("get_media_comments"):
        user = command.split(" ")[1]
        comments = bot.get_media_comments(user)
        print(f"{user}'ın son gönderisine yapılan yorumlar:", comments)

    elif command.startswith("get_user_likes"):
        user = command.split(" ")[1]
        likes = bot.get_user_likes(user)
        print(f"{user}'ın beğendiği gönderiler:", likes)

    elif command.startswith("mute"):
        user = command.split(" ")[1]
        bot.mute(user)
        print(f"{user}'ın bildirimleri sessize alındı.")

    elif command.startswith("unmute"):
        user = command.split(" ")[1]
        bot.unmute(user)
        print(f"{user}'ın bildirim sessizliği kaldırıldı.")

    elif command.startswith("share_post"):
        user = command.split(" ")[1]
        # Kullanıcının son gönderisini paylaşma işi burada olacak
        print(f"{user}'ın son gönderisi paylaşıldı.")  # Bu kısım kütüphaneye göre değişebilir.

    elif command.startswith("send_location"):
        parts = command.split(" ")
        user = parts[1]
        location = " ".join(parts[2:])
        # Belirtilen kullanıcıya konum gönderme işi burada olacak
        print(f"{user}'a konum gönderildi: {location}")  # Bu kısım kütüphaneye göre değişebilir.

    elif command.startswith("clear_chat"):
        user = command.split(" ")[1]
        # Kullanıcı ile sohbeti temizleme işi burada olacak
        print(f"{user} ile olan sohbet temizlendi.")  # Bu kısım kütüphaneye göre değişebilir.

    elif command == "get_saved_media":
        saved_media = bot.get_saved_media()
        print("Kaydedilmiş gönderiler:", saved_media)

    elif command.startswith("view_story"):
        user = command.split(" ")[1]
        # Kullanıcının hikayesini görüntüleme işi burada olacak
        print(f"{user}'ın hikayesi görüntülendi.")  # Bu kısım kütüphaneye göre değişebilir.

    elif command.startswith("schedule_post"):
        parts = command.split(" ")
        user = parts[1]
        date = parts[2]  # Tarih formatı burada belirlenmeli
        message = " ".join(parts[3:])
        # Belirtilen tarihte gönderi paylaşma işi burada olacak
        print(f"{user} için {date} tarihinde gönderi paylaşılacak: {message}")  # Bu kısım kütüphaneye göre değişebilir.

    elif command == "exit":
        bot.logout()
        print("Çıkış yapıldı.")
        break

    else:
        print("Geçersiz komut. Daha fazla bilgi için 'help' yazın.")
