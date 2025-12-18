tamam sana dersle alakalı her şeyi veriyorum ve seçtiğimiz komuyla alaklı bilgieri veriyorum buna göre ayrıntılı bir plan hazırla : MAT353 – Nümerik Analiz Dersi Dönem Projesi
PROJE ADINIZ (İLGİ
ÇEKİCİ VE KONUYU
İÇEREN BİR BAŞLIK)
MAT353 NÜMERİK ANALİZ DERSİ PROJE RAPORU

ADINIZ SOYADINIZ
ÖĞRENCI NUMARANIZ

ÖZET
Bu bölümde proje çalışmasının amacı, ele alınan problemin genel çerçevesi, kullanılan
nümerik yöntemler ve elde edilen temel bulgular özlü ancak kapsayıcı biçimde sunulmalıdır.
Özet, okuyucunun raporun tamamını okumadan çalışmanın kapsamını ve katkısını
anlayabileceği nitelikte olmalıdır. Kullanılan yöntemlerin adı açıkça belirtilmeli, uygulama
alanı (fizik, mühendislik vb.) net bir şekilde ifade edilmelidir. Bu bölümde referans
verilmemelidir ve uzunluk yaklaşık 200–250 kelime arasında olmalıdır.

GİRİŞ
Bu bölümde ele alınan problem açık, net ve bağlamı ile birlikte tanıtılmalıdır. Problemin
hangi fiziksel, mühendislik veya bilimsel ihtiyaca karşılık geldiği açıklanmalı; problemin neden
önemli olduğu ve gerçek dünyadaki karşılığı vurgulanmalıdır. Ardından literatürde bu
problemin veya benzer problemlerin nasıl ele alındığı özetlenmeli ve en az üç adet bilimsel
çalışma (makale, kitap bölümü veya konferans bildirisi) IEEE stilinde referans verilerek
tartışılmalıdır. Literatürde kullanılan yöntemlerin güçlü ve zayıf yönlerine değinilmesi
beklenmektedir. Son olarak, bu projede seçilen yöntemin neden uygun olduğu, hangi
açılardan literatürdeki çalışmalardan ayrıldığı veya onları nasıl geliştirdiği akademik bir dille
gerekçelendirilmelidir.

YÖNTEM
Bu bölüm projenin en kritik kısımlarından biridir. Kullanılan nümerik yöntem veya yöntemler
ayrıntılı biçimde açıklanmalı ve mutlaka matematiksel ifadelerle desteklenmelidir.
Problemin matematiksel modeli kurulmalı, kullanılan formüller, türevler, yaklaşık çözüm
yaklaşımları ve algoritmik adımlar açıkça sunulmalıdır. Yöntemin işleyişini netleştirmek
amacıyla akış diyagramları veya algoritma şemaları kullanılabilir. Bu bölümde kullanılan
yazılım ve donanım teknolojileri (örneğin NumPy, SciPy, JAX, GPU hızlandırma,
vektörleştirme yaklaşımları) açıkça belirtilmeli ve bu teknolojilerin neden tercih edildiği
gerekçelendirilmelidir.

UYGULAMA
Bu bölümde geliştirilen yöntemin Python ortamında nasıl hayata geçirildiği detaylı olarak
anlatılmalıdır. Kullanılan veri seti tanıtılmalı; veri seti öğrenciler tarafından oluşturulduysa
üretim süreci açıklanmalıdır. Kodların yalnızca nümerik yöntemele ilişki kodları sunulabilir,
ancak burada algoritmanın adım adım nasıl uygulandığı açıklanmalıdır. Uygulama sürecinde
yapılan varsayımlar, parametre seçimleri ve sayısal hassasiyet tercihleri belirtilmelidir. Ayrıca
hata analizi yapılmalı, farklı parametre veya yöntemlerle elde edilen sonuçlar
karşılaştırılmalıdır. Sonuçların görsel olarak anlaşılabilmesi için Matplotlib veya Seaborn
kullanılarak oluşturulmuş grafikler bu bölümde sunulmalıdır.

DENEYSEL SONUÇLAR
Bu bölümde elde edilen sonuçlar tablo ve grafiklerle sistematik biçimde sunulmalıdır.
Yöntemin doğruluğu, yakınsama davranışı ve sayısal performansı değerlendirilmelidir.
Gerekli durumlarda farklı yöntemler veya parametreler arasındaki doğruluk karşılaştırmaları
yapılmalıdır. İterasyon sayıları, hata eğrileri ve yakınsama grafikleri açıkça gösterilmelidir.
Eğer GPU veya hızlandırma teknikleri kullanıldıysa, CPU–GPU karşılaştırmaları veya çalışma
süresi analizleri de bu bölümde sunulabilir. Sunulan tüm tablolar ve şekiller metin içerisinde
mutlaka yorumlanmalıdır.

TARTIŞMA
Bu bölümde elde edilen deneysel sonuçların ne anlama geldiği akademik bir bakış açısıyla
yorumlanmalıdır. Yöntemin hangi koşullarda başarılı olduğu, hangi durumlarda sınırlı kaldığı
tartışılmalıdır. Sayısal kararlılık, hesaplama maliyeti ve doğruluk açısından güçlü ve zayıf
yönler açıkça ifade edilmelidir. Ayrıca, alternatif bir nümerik yöntem kullanılsaydı sonuçların
nasıl değişebileceği üzerine analitik ve eleştirel bir değerlendirme yapılması beklenmektedir.
Bu bölüm, sonuçların sadece tekrarlandığı değil, yorumlandığı bir bölüm olmalıdır.

TEST SÜREÇLERİ
Bu bölümde yazılımın doğrulanması ve hatalardan arındırılması için izlenen test yaklaşımı
açıklanmalıdır. Hangi test türlerinin uygulandığı, testlerin hangi aşamalarda gerçekleştirildiği
ve test kapsamının nasıl belirlendiği ifade edilmelidir. Birim testlerine ait örnekler sunulmalı
ve test edilen fonksiyonların beklenen çıktıları açıklanmalıdır. API kullanılan projelerde
Postman veya benzeri araçlarla yapılan testlere ait ekran görüntüleri eklenmelidir. Süreç
boyunca karşılaşılan hatalar, bu hataların nedenleri ve nasıl giderildiği açıklanarak yazılımın
olgunlaşma süreci ortaya konulmalıdır.

SONUÇ VE ÖNERİLER
Bu bölümde projenin genel bir değerlendirmesi yapılmalı ve çalışmanın temel katkıları
özetlenmelidir. Elde edilen sonuçların problem bağlamındaki önemi vurgulanmalı ve
çalışmanın hangi açılardan başarılı olduğu ifade edilmelidir. Bunun yanında, yöntemin veya
uygulamanın nasıl geliştirilebileceğine dair somut öneriler sunulmalıdır. Gelecekte
yapılabilecek çalışmalar, farklı veri setleri, farklı nümerik yöntemler veya daha gelişmiş
donanım kullanımı gibi başlıklar bu bölümde ele alınabilir.

KAYNAKÇA
Bu bölümde rapor boyunca kullanılan tüm kaynaklar IEEE referans stiline uygun olarak listelenmelidir.
Kaynaklar:
 Metin içinde numaralandırılarak gösterilmeli ([1], [2], …),
 Kaynakça bölümünde aynı numaralarla sıralanmalıdır.
Öğrenciler, özellikle akademik makaleleri, resmi dokümantasyonları ve güvenilir açık kaynakları tercih
etmelidir.
Proje Teslimi
: 21 Aralık Pazar saat 22.00

Proje Teslim Yeri
: Google Classroom

Teslim Edilecek Dosyalar : Proje Raporu, Sunum dosyası, Colab dosyası

Proje Sunumları
: 24 Aralık Çarşamba – 31 Aralık Çarşamba – 7 Ocak Çarşamba (Kimlerin
ne zaman sunacakları 17 Aralık günü derste kura yöntemiyle belirlenecektir)

Proje sunumu yapılmayan projeler teslim edilmemiş olarak değerlendirilecektir.

Proje Türü
: Bireysel, iki kişilik ya da üç kişilik projeler. Ekip üyeleri teslimde ve
sunumda birlikte sorumludur. 3 Aralık günü derste ekip üyelerinin bilgileri alınacaktır.

Projenin Amacı
: Bu dönem projesinin amacı, öğrencilerin dönem boyunca öğrendikleri
nümerik yöntemleri gerçek bir probleme uygulamalarını sağlamaktır.

Proje basit bir ödev değildir; bir mini araştırma projesidir. Ders notunun %18’ini kapsar.

MAT353 – Nümerik Analiz Dersi Dönem Projesi

Öğrenciler:

Fizik, mühendislik gibi alanlarda bir probleme yönelik çözümü oluşturacaklardır.

Basit uygulamalar kabul edilmeyecektir. Projede modern teknolojiler kullanmalı ve
özgün bir problem çözmelidir.

MAT353 – Nümerik Analiz Dersi Dönem Projesi

Öğrenciler proje konusunu kendileri belirler.
Örnek konu başlıkları (bu konular seçilmeyecektir)

Serbest Düşme ve Terminal Hızın Nümerik Hesaplanması

Tek Boyutlu Isı Yayılımının (Heat Equation) Sonlu Farklar Yöntemi ile Simülasyonu

Dirençli Dikey Atış Hareketinin Nümerik Çözümü ve Zaman Adımı Analizi

Newton Yöntemi ile Doğrusal Olmayan Yay Kuvveti Probleminin Çözümü

Araba Fren Mesafesinin Sürtünme ve Direnç Kuvvetleri Altında Nümerik Hesaplanması

Basit örnekler kabul edilmez.

MAT353 – Nümerik Analiz Dersi Dönem Projesi

Proje Raporu İçeriği (Zorunlu Yapı)

1. Kapak

2. Giriş (1–2 sayfa)

Problemin tanıtımı

Literatürde bu problemin nasıl çözüldüğü (en az 3 bilimsel kaynak)

Seçilen yöntemin neden uygun olduğu

3. Yöntem (2–4 sayfa)

Bu bölüm mutlaka matematiksel ifadeler içermelidir:

Kullanılan nümerik yöntem(ler)

Formüller, türev, akış diyagramları

Karmaşıklık analizi (Big-O)

Kullanılan teknolojiler (NumPy, SciPy, JAX, GPU vs.)

4. Uygulama (2–4 sayfa)

Python kodları (Appendix’e alınabilir)

Kullanılan veri seti (kendi oluşturduğu olabilir)

Adım adım açıklama

Hata analizi, karşılaştırmalar

Grafikler (Matplotlib/Seaborn)

5. Deneysel Sonuçlar (1–3 sayfa)

Tablo ve grafiklerle:

doğruluk karşılaştırmaları

iterasyon sayıları

hata eğrileri

performans ölçümleri (isteğe bağlı GPU
hızlandırma)

6. Tartışma

Elde edilen sonuçlar ne anlama geliyor?

Yöntemin güçlü/zayıf yönleri

Alternatif yöntem kullanılsa ne olurdu?

7. Sonuç ve Öneriler

Projenin genel değerlendirmesi

Geliştirme önerileri

8. Kaynakça

IEEE stile uygun.

MAT353 – Nümerik Analiz Dersi Dönem Projesi

Proje Sunumu

Her ekip 15 dakika sunum yapacaktır.

Sunum içeriği:

Problem ve amaç

Yöntem

Matematiksel altyapı

Uygulama ve sonuçlar

Tartışma ve öneriler

Ekip üyeleri görev dağılımı / yapılan işler

Sunum kuralları:

En fazla 10 slayt

Her slayt sade ve anlaşılır olmalı

Demosu çalışmayan uygulamalara puan kesintisi uygulanacaktır

MAT353 – Nümerik Analiz Dersi Dönem Projesi

Bölüm

Açıklama

Puan

Proje Özgünlüğü ve Zorluk Düzeyi

Konunun derinliği, kullanılan teknolojinin seviyesi, özgün yaklaşım

20 P

Matematiksel Modelleme ve Teorik Çerçeve

Formüller, türevler, hata analizleri, ispatlar, akış diyagramları

15 P

Yöntemlerin Doğru Uygulanması

Nümerik yöntemlerin doğru yazılması, test edilmesi

15 P

Python Uygulaması

Kod kalitesi, fonksiyonel yapı, yorum satırları, performans

15 P

Sonuçlar ve Grafiksel Analiz

Tablolar, hata eğrileri, karşılaştırmalar, bilimsel yorumlama

10 P

Raporun Kalitesi

Akademik yazım, düzen, kaynakça, 8–15 sayfa uygunluğu

10 P

Sunum Performansı

İfade becerisi, süreye uyma, slayt tasarımı, teknik açıklamalar

15 P Değerli Öğrencilerim,
Dönem projelerinizi 21 Aralık Pazar günü saat 22.00'ye kadar buradan yükleyebilirsiniz. Yükleyeceğiz belgeler;
1-Projenin çalışır ve paylaşılmış durumda bir Colab dosyası. Colab dosyasındaki hücreler önceden çalıştırılmış ve çıktıları üretilmiş olmalıdır (grafik, print vb.) İlgili dosya Colab üzerinde direk çalışabilir şekilde olmalı, dosya adı kimliğinizde olduğu şekilde herhangi bir kısaltma vb. olmadan kullanılmalıdır.
2- Proje raporu ekte sunulan rapor formatında hazırlanmalıdır. Belirtilen başlıkların altındaki içeriklerin doldurulması gerekmektedir. İçerikteki yazılar Calibri 12 pt boyutunda, her iki yana yaslı yapılmalıdır. Resim ve grafikler sayfaya ortalanmalıdır. Kaynakçada IEEE stili kullanılmalıdır. Kapak kısmında projenin github linki eklenecektir. Proje grup olarak yapıldıysa kapak kısmında öğrencilerin ad soyad ve numaraları formatta gösterildiği şekilde belirtilmelidir. Raporunuz PDF formatında ve dosya adı kimliğinizde olduğu şekilde herhangi bir kısaltma vb. olmadan kullanılmalıdır.
3- Sunum dosyası için bir şablon sunulmamıştır. Sunumunuzun 15 dakika ile sınırlı olduğunu düşünerek projeniz ile ilgili açıklanması gereken kısımları belirtmeniz sağlıklı olacaktır. Sunum dosyanız PPT formatında ve dosya adı kimliğinizde olduğu şekilde herhangi bir kısaltma vb. olmadan kullanılmalıdır.

Belirtilen dosyaların zamanında (21 Aralık Pazar günü saat 22.00'ye kadar) gönderilmemesi durumunda sunum yapılamayacaktır.
Başarılar dilerim. porje konumuz bu tarz bir şey olabilir yani linner regrsyonu hem en küçğk karaeler hem gradient descent ile çözme sonra oradaki merkezi türev vs nümerikle alaklı olan kısımlar  bu iki alt projeyi yapıcaz A) Alt Proje 1 — Doğrusal regresyon: Normal Denklem vs Gradient Descent
1) Problem tanımı

Veri: Sentetik + 1 küçük gerçek veri (ör. California housing gibi)
Amaç: 
min
⁡
𝜃
𝐽
(
𝜃
)
=
1
2
𝑛
∥
𝑋
𝜃
−
𝑦
∥
2
2
min
θ
	​

J(θ)=
2n
1
	​

∥Xθ−y∥
2
2
	​


2) Matematiksel altyapı (rapora koyacağın ana türetim)

Normal denklem: 
∇
𝜃
𝐽
(
𝜃
)
=
0
⇒
𝑋
𝑇
𝑋
𝜃
=
𝑋
𝑇
𝑦
∇
θ
	​

J(θ)=0⇒X
T
Xθ=X
T
y

Çözüm (invert etmek yerine pratikte “solve” vurgusu): 
𝜃
\*
=
(
𝑋
𝑇
𝑋
)
−
1
𝑋
𝑇
𝑦
θ
\*
=(X
T
X)
−1
X
T
y

GD güncellemesi: 
𝜃
𝑘
+
1
=
𝜃
𝑘
−
𝛼
∇
𝐽
(
𝜃
𝑘
)
θ
k+1
	​

=θ
k
	​

−α∇J(θ
k
	​

),

∇
𝐽
(
𝜃
)
=
1
𝑛
𝑋
𝑇
(
𝑋
𝜃
−
𝑦
)
∇J(θ)=
n
1
	​

X
T
(Xθ−y)

3) Nümerik analiz / stabilite kısmı (projeyi “basit” olmaktan çıkaran nokta)

Koşullanma deneyi: Özellikleri birbirine çok kolinear yap (ör. 
𝑥
2
=
𝑥
1
+
10
−
𝑝
𝜉
x
2
	​

=x
1
	​

+10
−p
ξ).

𝑝
p arttıkça 
𝑋
𝑇
𝑋
X
T
X kötü koşullu olur; normal denklem sayısal olarak bozulabilir.

Çözüm varyantları:

Inverse ile çöz (bilerek “kötü pratik” olarak)

np.linalg.solve ile çöz (daha iyi) 

Ders 8

(opsiyonel) QR ile çöz (en stabil anlatım)

4) Deney metrikleri

MSE / RMSE (train/val)

GD için: iterasyon sayısı, loss eğrisi, 
∥
∇
𝐽
∥
∥∇J∥ eğrisi

Zaman: 
𝑑
d ve 
𝑛
n büyürken runtime karşılaştırması

5) Karmaşıklık (Big-O)

Normal denklem (naif): 
𝑋
𝑇
𝑋
X
T
X hesaplama 
𝑂
(
𝑛
𝑑
2
)
O(nd
2
), çözüm/invers 
𝑂
(
𝑑
3
)
O(d
3
)

GD: her iterasyon 
𝑂
(
𝑛
𝑑
)
O(nd), toplam 
𝑂
(
𝑘
𝑛
𝑑
)
O(knd) (k iterasyon)

Kaynak desteği için normal equation vs GD farklarını anlatan bir referans kullanabilirsin. 
DataCamp
+1

B) Alt Proje 2 — Gradient Checking (Sayısal vs Analitik gradyan)
1) Problem tanımı

İki seçenekten biri yeterli:

(kolay ve temiz) Logistic regression (tek katman)

(daha “DL kokan”) 2-layer küçük NN (NumPy ile)

2) Sayısal gradyan (derse direkt bağlı nokta)

Merkezi fark:

∂
𝐽
(
𝜃
)
∂
𝜃
𝑖
≈
𝐽
(
𝜃
𝑖
+
𝜀
)
−
𝐽
(
𝜃
𝑖
−
𝜀
)
2
𝜀
∂θ
i
	​

∂J(θ)
	​

≈
2ε
J(θ
i
	​

+ε)−J(θ
i
	​

−ε)
	​


Merkezi farkın kesme hatası mertebesi 
𝑂
(
𝜀
2
)
O(ε
2
) (raporda mutlaka yaz). 
Institute for Advanced Study

Derste de “merkezi fark daha doğru” vurgusu var. 

Ders 2

3) Karşılaştırma metriği

Relative error öner:

relerr
=
∣
𝑔
analytic
−
𝑔
num
∣
max
⁡
(
∣
𝑔
analytic
∣
,
∣
𝑔
num
∣
)
relerr=
max(∣g
analytic
	​

∣,∣g
num
	​

∣)
∣g
analytic
	​

−g
num
	​

∣
	​


Gradient check’in pratik anlatımı için referans: 
CS231n
+1

4) “Mini araştırma” yapan deney: epsilon taraması

𝜀
∈
{
10
−
1
,
10
−
2
,
.
.
.
,
10
−
10
}
ε∈{10
−1
,10
−2
,...,10
−10
} için relerr grafiği çiz:

Büyük 
𝜀
ε: truncation baskın

Çok küçük 
𝜀
ε: rounding baskın
Bu tartışma doğrudan “sayısal hata türleri” bölümüne oturur.


BU PROJE BENİM NÜMERİK ANALİZ DERSİNDE GÖRDÜĞÜM ŞEYLER İLE UYUMLU MU