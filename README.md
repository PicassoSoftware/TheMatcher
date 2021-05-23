# OTOMATA PROJESİ
## *The Matcher*
> Kullanıcının belirlediği _Regular Express_ şartlarına uygun nfa ve dfa bilgisi elde edilir. Verilen metin içerisinde uygunluk kontrol edilir.

<br>
<br>

### **Yapılanlar**
- [x] Düzenli ifade ve arama yapılacak metin _GUI_ üzerinden alınabilir hale geldi. 
- [x] Gui üzerinden alınan her `RE'`nin hem `NFA'e` hem de `DFA'e` dönüşümü sağlandı. **Bu dönüşümde hazır kütüphanelerden yararlanılmadı.**
- [x] Dinamik olarak `RE'`nin `NFA` ve `DFA` karşılığı, seçime göre ekranda koşulur hale geldi. Bu işlem yapılırken aynı zamanda, işlem gören metin rengi değiştirilerek belirgin hale getirildi.
- [x] Metin ile formal bilginin eşleşmesi durumunda rengi değiştirilerek, prosedüre uygun olduğu belirtildi.


<br>
<br>
<br>

Öğrenci No | Adı Soyadı | Görevi
------------ | ------------- | -------------
383183 | Hatice Kovan | **GUI** ekranının yapılması. |
383201 | *__Neziha Esra Bilgili__* | Metin içinde aranan kelimenin uyuşma durumuna göre **rengini** değiştirmek. |
383221 | Sırat Semih Çöp | Elde edilen **Formal** bilgi ile başarılı veya başarısız durum bilgisini oluşturmak. |
383245 | Furkan Sefa Demirci | **NFA**, **DFA** çizimi ve durum değişimlerinin dinamik olarak gösterilmesi. |
394783 | Sema Nur Boz | **NFA**'den **DFA** oluşturmak. |
399605 | Erkin Abuzarli | Verilen **RegEx**’i **NFA**’e dönüştürmek.  |


<br>
<br>
<br>

## GUI VE KULLANIMI
##### Gif eklenecek.
<br>
<br>
- Gui dosyasını çalıştırdığımızda açılan ekranda regex etiketli kısıma aratmak istediğiniz ifadeyi giriniz. 

- Metin etiketli kısma regexi içinde aratacağınız metni giriniz. 

- Open File kısmından aratmak istediğiniz metin dosyasını seçerek text kutusuna ekleyebilirsiniz. 

- Daha sonra NFA, DFA butonlarından stateni görmek istediğiniz durumu seçiniz. Seçtiğiniz butonun rengi değişiyorsa bu o işlemi gerçekleştireceğinizi belirtmektedir. İlk ekran açıldığında Dfa butonu basılı halde gelecektir. 

- Start butonuna bastığınızda ifadeniz metin içerisinde aranmaya ve bununla birlikte state durumları gösterilme başlayacaktır. 

- Metin içerisinde arama işlemi yapılırken ilk başta incelenen kelime sarı renk olacaktır. Eğer aranan kelime ile incelenen kelime uyuşuyorsa kelimemiz yeşil renge, uyuşmuyorsa beyaz rengine dönecektir. 

- Sarıya dönen kelimemiz içerinde gezinirken sağ taraftaki statemiz de bu işlemle senkron bir şekilde arama işlemini gerçekleştirmeye başlar ve bu her kelime için tekrarlanır. Aranan durum tek tek gezinerek state te turuncu renkle gösterilmektedir. 

- Stop tuşuna bastığımızda aranılan kelime için işlem yapılır ve sonra olaylar durur. NFA/DFA ve Start buton renkleri sıfırlanır. 


