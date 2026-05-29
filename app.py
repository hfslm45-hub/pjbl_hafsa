import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "🔥"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("logo.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Belah Ketupat", "Segitiga"])
    st.caption("Dibuat dengan :fire: oleh **Hafsa Lanika Mahani**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            st.success(f"Luas Persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.snow()


    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung 'luas' dan 'keliling' Persegi Panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            st.success(f"Luas Persegi Panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung 'luas' dan 'keliling' Lingkaran")
        jarijari = st.number_input("Masukkan Jari-jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari
            st.success(f"Luas Lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()

    case "Belah Ketupat":
        st.title("Belah Ketupat")
        st.markdown("Menghitung 'luas' dan 'keliling' Belah Ketupat")
        diagonal1 = st.number_input("Masukkan Diagonal 1")
        diagonal2 = st.number_input("Masukkan Diagonal 2")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * diagonal1 * diagonal2
            keliling = 4 * sisi
            st.success(f"Luas Belah Ketupat adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.balloons()


    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung 'luas' dan 'keliling' Segitiga")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi1 = st.number_input("Masukkan Sisi 1")
        sisi2 = st.number_input("Masukkan Sisi 2")
        sisi3 = st.number_input("Masukkan Sisi 3")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi1 + sisi2 + sisi3
            st.success(f"Luas Segitiga adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            st.snow()

    case _ :
        st.error("Terjadi kesalahan")
