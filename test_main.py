from main import xac_dinh_kha_nang_vay

import pytest

@pytest.mark.parametrize(
    "tuoi,thu_nhap,expected_result",
    [
        (-1,100,"Input không hợp lệ"),
        (20,-1,"Input không hợp lệ"),
        (10,100,"Không được vay"),
        (20,2,"Không được vay"),
        (20,12,20),
        (20,20,40),
        (20,40,60),
        (20,90,80),
        (40,2,"Không được vay"),
        (40,12,"Không được vay"),
        (40,20,20),
        (40,40,40),
        (40,90,60),
        (50,2,"Không được vay"),
        (50,12,"Không được vay"),
        (50,20,"Không được vay"),
        (50,40,20),
        (50,90,40),
        (70,50,"Không được vay"),
    ]
)
def test_xac_dinh_kha_nang_vay_theo_bang_quyet_dinh(tuoi, thu_nhap, expected_result):
    actual_result = xac_dinh_kha_nang_vay(tuoi, thu_nhap)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    "tuoi,thu_nhap,expected_result",
    [
        (-1,-1,"Input không hợp lệ"),
        (10,2,"Không được vay"),
        (20,12,20),
        (40,20,20),
        (50,40,20),
        (70,90,"Không được vay")
    ]
)
def test_xac_dinh_kha_nang_vay_theo_phan_hoach(tuoi, thu_nhap, expected_result):
    actual_result = xac_dinh_kha_nang_vay(tuoi, thu_nhap)

    assert actual_result == expected_result


