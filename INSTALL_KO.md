# 설치 안내

## 1. 준비물

- 대상 일본판 GBA ROM
- `xdelta3`
- 이 저장소 루트의 `Tales_of_the_World_Summoners_Lineage_KO.xdelta`

원본 ROM은 이 저장소에서 제공하지 않습니다.

## 2. 원본 확인

PowerShell:

```powershell
Get-FileHash "Tales of the World - Summoner's Lineage (Japan).gba" -Algorithm SHA256
```

정상 SHA-256:

```text
b41c293fc0ed6111b7a37d960d9cd0c685e5d521a4739e0e2eaa7ff6186cfdd3
```

해시가 다르면 적용하지 마십시오.

## 3. 자동 적용과 검증

`xdelta3`가 PATH에 등록되어 있다면 다음 명령을 실행합니다.

```powershell
python scripts/apply_patch.py "Tales of the World - Summoner's Lineage (Japan).gba"
```

기본 출력 파일은 `summoners_lineage_ko.gba`입니다. 다른 경로를 지정하려면 두 번째 인수를 사용합니다.

```powershell
python scripts/apply_patch.py "원본.gba" "내 폴더/서머너즈 리니지 한국어.gba"
```

`xdelta3` 실행 파일이 PATH에 없다면 `--xdelta`로 위치를 지정할 수 있습니다.

```powershell
python scripts/apply_patch.py "원본.gba" --xdelta "C:\Tools\xdelta3.exe"
```

## 4. 직접 적용

```powershell
xdelta3 -d -s "Tales of the World - Summoner's Lineage (Japan).gba" `
  "Tales_of_the_World_Summoners_Lineage_KO.xdelta" `
  "summoners_lineage_ko.gba"
```

## 5. 결과 확인

```powershell
Get-FileHash "summoners_lineage_ko.gba" -Algorithm SHA256
```

정상 결과:

```text
크기     9,023,416 bytes
SHA-256  ba353cfd547db33460711065cefec526920e39e4a09f2e3d4a3883c5ee36bc9e
```

## 6. 실행

패치된 ROM을 GBA 에뮬레이터에서 엽니다. 제작 검증에는 mGBA를 사용했습니다. 기존 일본판 세이브를 쓰기 전에는 별도 백업을 권장합니다.
