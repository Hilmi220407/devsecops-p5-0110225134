def validate_title(title):
    """Judul tidak boleh kosong dan maksimal 100 karakter."""
    if not isinstance(title, str):
        return False
    title = title.strip()
    return 0 < len(title) <= 100


def count_done(tasks):
    """Hitung jumlah task yang sudah selesai."""
    return sum(1 for t in tasks if t.done)