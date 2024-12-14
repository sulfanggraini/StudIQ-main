document.getElementById("lihatMateriButton").addEventListener("click", function (event) {
    event.preventDefault(); // Mencegah tindakan default

    const kelas = document.getElementById("kelasSelect").value;
    const mapel = document.getElementById("mapelSelect").value;

    if (kelas === "Pilih Kelas" || mapel === "Pilih Mata Pelajaran") {
        alert("Silakan pilih kelas dan mata pelajaran terlebih dahulu.");
        return;
    }

    // Susun URL tujuan dengan parameter
    const targetPage = `materi/${kelas}/${mapel}/`;

    // Alihkan ke halaman tujuan
    window.location.href = targetPage;
});