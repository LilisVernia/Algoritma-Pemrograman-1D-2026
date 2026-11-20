undangan = set()
webinar_a = set()
webinar_b = set()

print("DAFTAR UNDANGAN")
undangan.add(input("Nama undangan 1: "))
undangan.add(input("Nama undangan 2: "))
undangan.add(input("Nama undangan 3: "))
undangan.add(input("Nama undangan 4: "))

print("PESERTA WEBINAR A")
webinar_a.add(input("Nama peserta 1: "))
webinar_a.add(input("Nama peserta 2: "))
webinar_a.add(input("Nama peserta 3: "))

print("PESERTA WEBINAR B")
webinar_b.add(input("Nama peserta 1: "))
webinar_b.add(input("Nama peserta 2: "))
webinar_b.add(input("Nama peserta 3: "))

print("HASIL WEBINAR")

print("Semua peserta:", webinar_a.union(webinar_b))

print("Hadir di kedua webinar:",
      webinar_a.intersection(webinar_b))

print("Hadir di salah satu webinar:",
      webinar_a.symmetric_difference(webinar_b))

print("Undangan tidak hadir:",
      undangan.difference(webinar_a.union(webinar_b)))