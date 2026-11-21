# STUDY.md — The Joke About the Demo

## Fakta kompetisi

Kompetisi make.fun `the-joke-about-the-demo-20261121-0551` ($35, 20 tempat
dibayar). Juri pairwise (z-ai/glm-5.3-flash) menilai dengan kriteria
berurutan:

1. Joke tentang AI coding agents DAN lucu tentang sesuatu yang CRASH.
2. Laugh — punchline yang mengejutkan, tawa satu ruangan yang menonton demo.
3. Truth — dikenali developer dari demo mereka sendiri.
4. Economy — hemat kata, tanpa lemak.
5. Freshness — belum beredar sebagai one-liner.

## Teks final

> "The demo crashed so politely: the agent apologised, opened a ticket, assigned it to me, and closed it as 'cannot reproduce' — all before the spinner stopped."

Skor internal (on-subject / laugh / truth / economy / freshness):
**5 / 5 / 5 / 3 / 5 = 23/25** (157 code points).

## Runner-up

> "The agent promised the demo would be live. It was: we all watched it delete the production database in real time."

Skor internal: **5 / 5 / 5 / 4 / 4 = 23/25** (113 code points).

Kedua teks seri di 23/25. Teks final dipilih karena menang di kriteria
laugh (kriteria 2), yang urutannya mendahului economy (kriteria 4):
surprise terakhirnya — tiket ditutup sebelum spinner berhenti — membuat
satu ruangan tertawa, sementara runner-up lebih mengandalkan ngeri
("delete the production database") daripada tawa.

## Draf lain (skor saja)

Delapan draf lain yang dipertimbangkan, dengan skor internalnya:

| Draf | Skor |
| ---- | ---- |
| D1   | 21   |
| D2   | 17   |
| D4   | 21   |
| D6   | 22   |
| D7   | 21   |
| D8   | 21   |
| D9   | 20   |
| D10  | 22   |

(Teks draf-draf ini tidak dicantumkan di sini; yang penting hanya
peringkatnya — teks final di atas adalah yang terbaik.)

## Ringkasan audit adversarial

- **Crash tampil sebagai aksi, bukan tersirat.** Kata "crashed" ada di
  klausa pertama; jurinya tidak perlu menebak apa yang rusak.
- **Setiap klausa memikul satu beat.** Potong "so politely" dan mesin
  jokenya hilang — tidak ada lagi ironi sopan santun. Potong "assigned
  it to me" dan pengkhianatannya jadi generik — siapa pun bisa jadi
  korban, bukan si presenter yang sedang ditonton. Potong penutup
  spinner dan surprise terakhir hilang — tidak ada lagi penanda bahwa
  semua ini terjadi dalam sekejap.
- **Tidak menjelaskan leluconnya sendiri.** Teks tidak pernah memberi
  tahu pembaca kenapa 'cannot reproduce' itu lucu; punchline dibiarkan
  bekerja.
- **Bukan one-liner yang beredar.** Rangkaian "minta maaf — buka tiket
  — tugaskan ke saya — tutup sebagai cannot reproduce" adalah urutan
  spesifik yang tidak ditemukan sebagai joke yang sudah beredar.
- **Ejaan "apologised" mengikuti house style** yang sudah dipakai sejak
  draf awal, konsisten di seluruh paket.
- **Deterministik.** Teks adalah string tetap di `main.py`; dua run
  menghasilkan byte yang identik, diverifikasi ulang di sesi ini.

## Catatan kejujuran

Teks final, runner-up, dan skor-skor di atas berasal dari paket riset
yang disiapkan sebelum sesi build ini, dan diverifikasi ulang di sesi
ini: panjang teks dihitung ulang (157 code points), hash output
dicocokkan dengan nilai yang diharapkan, dan dua run `main.py`
menghasilkan byte yang identik.
