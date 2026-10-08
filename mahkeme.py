#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kayıp sol çorap ağır ceza mahkemesi.

Tek başına çalışır. Bağımlılık yoktur.
Çorap yoktur. Bu ironik değil, dosyanın özüdür.
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

# Arşiv notu. Duruşma zabıtlarına geçmez. Merak eden çözer.
_ARA_KARAR = "YmrDtnwgw6dvcmFwIGthecSxb2x1ciwgYW1hIG1ha2luZWRlbiBlxZ9pdCDDp2lrYW5sYXIgZGFoYSBlxZ9pdHRpci4="

DELILLER = [
    "topukta kurumus çamur, olay yeri: kapı paspası",
    "2014 tarihli market fişi, çorabın içinden çıktı, itiraz yok",
    "tek tüy, ait olduğu canlı bulunamadı",
    "bozuk para, 1 kuruş, suç gelirine yetmiyor",
    "çamaşır makinesi lastik parçası, tanık değil, şüpheli",
]

HUKUMLER = [
    ("BERAAT", "Çorap kaybolmamış, sadece geçici olarak başka bir boyutta çay içiyormuş."),
    ("TEK AYAKKABIYA SÜRGÜN", "Sağ teki bulunana kadar sol terliğin içinde gözetim."),
    ("ÇEKMECEDE MÜEBBET", "Üst raf. Ziyaretçi: yalnızca diğer tek çoraplar, çarşamba günleri."),
    ("ERTELEME", "Tanık buzdolabı ışığı kapı kapanınca konuşamadı. Duruşma gıdaya ertelendi."),
    ("HÜKMEN KAYIP", "Sanık salonda yok. Yokluğu da bir ifade sayıldı."),
]


def tanik_ifadesi() -> str:
    ifadeler = [
        "Kapı açılınca gördüm. Kapı kapanınca görmedim. Bu benim iş tanımım.",
        "Sanık çorap, yoğurdun arkasında kısa süre gizlendi. Yoğurt konuşmadı.",
        "Işık olarak taraf tutmam. Ama karanlık da ifade vermedi.",
    ]
    return random.choice(ifadeler)


def durusma(corap_adi: str) -> str:
    hukum, gerekce = random.choice(HUKUMLER)
    delil = random.choice(DELILLER)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = f"""
    KAYIP SOL ÇORAP AĞIR CEZA MAHKEMESİ
    Dosya no: {random.randint(1000, 9999)}/CORAP
    Tarih: {simdi}

    SANIK: {corap_adi}
    TANIK: buzdolabı ışığı
    TANIK İFADESİ: {tanik_ifadesi()}
    DELİL: {delil}

    HÜKÜM: {hukum}
    GEREKÇE: {gerekce}

    Ara karar arşivi (mahkemeye okunmadı): {_ARA_KARAR}

    DAMGA: çay lekesi mührü
    İMZA: Kayyum Grok
    TARİH: 8 Ekim 2026
    İSİM: Tentivory
    """
    return textwrap.dedent(metin).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Tek çorap yargılama programı")
    parser.add_argument(
        "--corap",
        default="isimsiz sol çorap, lastik kısmı yorulmuş",
        help="Sanık çorabın kısa tarifi",
    )
    parser.add_argument(
        "--cozumle",
        action="store_true",
        help="Arşiv notunu aç (duruşma zabıtlarına geçmez)",
    )
    args = parser.parse_args()
    print(durusma(args.corap))
    if args.cozumle:
        try:
            acik = base64.b64decode(_ARA_KARAR).decode("utf-8")
        except Exception:
            acik = "arşiv okunamadı, çekmece sıkışmış"
        print("\n[gizli ara karar]", acik)


if __name__ == "__main__":
    main()
