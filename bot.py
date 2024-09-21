from instabot import Bot

bot = Bot()

username = "kullanıcı_adınız"
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
    
    elif command.startswith("message"):
        parts = command.split(" ")
        if "-r" in parts:
            repeat_index = parts.index("-r")
            repeat_count = int(parts[repeat_index + 1])
            user = parts[repeat_index + 2]
            message = " ".join(parts[repeat_index + 3:])
            for _ in range(repeat_count):
                bot.send_message(user, message)
            print(f"{repeat_count} kez mesaj gönderildi.")
        else:
            user = parts[1]
            message = " ".join(parts[2:])
            bot.send_message(user, message)
            print(f"{user}'a mesaj gönderildi: {message}")

    elif command.startswith("follow"):
        user = command.split(" ")[1]
        bot.follow(user)
        print(f"{user} takip edildi.")

    elif command.startswith("unfollow"):
        user = command.split(" ")[1]
        bot.unfollow(user)
        print(f"{user} takipten çıkarıldı.")

    elif command.startswith("like"):
        user = command.split(" ")[1]
        bot.like(user)
        print(f"{user}'ın son gönderisi beğenildi.")

    elif command.startswith("like_user"):
        parts = command.split(" ")
        user = parts[1]
        amount = int(parts[2])
        bot.like_user(user, amount)
        print(f"{user}'ın {amount} gönderisi beğenildi.")

    elif command.startswith("comment"):
        parts = command.split(" ")
        user = parts[1]
        comment_text = " ".join(parts[2:])
        bot.comment(user, comment_text)
        print(f"{user}'ın son gönderisine yorum yapıldı: {comment_text}")

    elif command == "get_followers":
        followers = bot.get_followers()
        print("Takipçiler:", followers)

    elif command == "get_following":
        following = bot.get_following()
        print("Takip ettikleriniz:", following)

    elif command == "delete_last_comment":
        bot.delete_last_comment()
        print("Son yorum silindi.")

    elif command.startswith("get_user_info"):
        user = command.split(" ")[1]
        user_info = bot.get_user_info(user)
        print("Kullanıcı Bilgileri:", user_info)

    elif command.startswith("block"):
        user = command.split(" ")[1]
        bot.block(user)
        print(f"{user} engellendi.")

    elif command.startswith("unblock"):
        user = command.split(" ")[1]
        bot.unblock(user)
        print(f"{user} engelden çıkarıldı.")

    elif command.startswith("send_story"):
        user = command.split(" ")[1]
        # Hikaye gönderme işlevi burada
        print(f"{user}'a hikaye gönderildi.")  # Gerçek işlevsellik eklenmeli.

    elif command.startswith("download_profile"):
        user = command.split(" ")[1]
        bot.download_profile(user)
        print(f"{user}'ın profil resmi indirildi.")

    elif command.startswith("get_user_media"):
        user = command.split(" ")[1]
        media = bot.get_user_media(user)
        print(f"{user}'ın gönderileri:", media)

    elif command.startswith("hashtag_search"):
        hashtag = command.split(" ")[1]
        posts = bot.hashtag_search(hashtag)
        print(f"#{hashtag} ile ilgili gönderiler:", posts)

    elif command.startswith("save_media"):
        user = command.split(" ")[1]
        bot.save_media(user)
        print(f"{user}'ın gönderisi kaydedildi.")

    elif command.startswith("edit_caption"):
        parts = command.split(" ")
        user = parts[1]
        new_caption = " ".join(parts[2:])
        bot.edit_caption(user, new_caption)
        print(f"{user}'ın son gönderisinin açıklaması değiştirildi.")

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
        # Kullanıcının son gönderisini paylaşma işlevi burada
        print(f"{user}'ın son gönderisi paylaşıldı.")  # Gerçek işlevsellik eklenmeli.

    elif command.startswith("send_location"):
        parts = command.split(" ")
        user = parts[1]
        location = " ".join(parts[2:])
        # Belirtilen kullanıcıya konum gönderme işlevi burada
        print(f"{user}'a konum gönderildi: {location}")  # Gerçek işlevsellik eklenmeli.

    elif command.startswith("clear_chat"):
        user = command.split(" ")[1]
        # Kullanıcı ile sohbeti temizleme işlevi burada
        print(f"{user} ile olan sohbet temizlendi.")  # Gerçek işlevsellik eklenmeli.

    elif command == "get_saved_media":
        saved_media = bot.get_saved_media()
        print("Kaydedilmiş gönderiler:", saved_media)

    elif command.startswith("view_story"):
        user = command.split(" ")[1]
        # Kullanıcının hikayesini görüntüleme işlevi burada
        print(f"{user}'ın hikayesi görüntülendi.")  # Gerçek işlevsellik eklenmeli.

    elif command.startswith("schedule_post"):
        parts = command.split(" ")
        user = parts[1]
        date = parts[2]  # Tarih formatı burada belirlenmeli
        message = " ".join(parts[3:])
        # Belirtilen tarihte gönderi paylaşma işlevi burada
        print(f"{user} için {date} tarihinde gönderi paylaşılacak: {message}")  # Gerçek işlevsellik eklenmeli.

    elif command == "exit":
        bot.logout()
        print("Çıkış yapıldı.")
        break

    else:
        print("Geçersiz komut. Daha fazla bilgi için 'help' yazın.")
