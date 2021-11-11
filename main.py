def xac_dinh_kha_nang_vay(tuoi, thu_nhap):
    if tuoi < 0 or thu_nhap < 0:
        return "Input không hợp lệ"
    elif tuoi < 18:
        return "Không được vay"
    elif tuoi < 35:
        if thu_nhap < 8:
            return "Không được vay"
        elif thu_nhap < 15:
            return 20
        elif thu_nhap < 30:
            return 40
        elif thu_nhap <= 50:
            return 60
        else:
            return 80
    elif tuoi < 45:
        if thu_nhap < 15:
            return "Không được vay"
        elif thu_nhap < 30:
            return 20
        elif thu_nhap <= 50:
            return 40
        else:
            return 60
    elif tuoi <= 60:
        if thu_nhap < 30:
            return "Không được vay"
        elif thu_nhap <= 50:
            return 20
        else:
            return 40
    else:
        return "Không được vay"