# 테일즈 오브 더 월드 ~서머너즈 리니지~ 한국어 패치

> **v1.0.1 공개 릴리스**

게임보이 어드밴스 일본판 `Tales of the World: Summoner's Lineage`용 비공식 한국어 현지화 패치 배포 저장소입니다.

- 게임 코드: `A9PJ`
- 대상 파일 크기: `8,388,608 bytes`
- 대상 원본 SHA-256: `b41c293fc0ed6111b7a37d960d9cd0c685e5d521a4739e0e2eaa7ff6186cfdd3`
- 준비 버전·태그: `v1.0.1`
- 저장소: `TeamLimRyan/TALES_OF_THE_WORLD_SUMMONERS_LINEAGE_KOREAN_LOCALIZATION_RELEASE`

## 포함 범위

- 원문 텍스트 5,822행 한국어 번역
- 캐릭터·클래스·스킬·아이템·시스템 고정 데이터 744레코드, 이름 필드 1,210개 반영
- 승인된 이미지 한글화 70개 반영
- 현대 한글 완성형 11,172자 글리프와 한글 조합식 이름 입력
- 55키 한글 자모 키보드와 한국어 버튼 표기
- 실제 mGBA에서 부팅, 메뉴, 이름 입력, 초반 대사 및 `임라이언` 조합 입력 검증

## 다운로드

최신 안정판은 [GitHub Releases의 v1.0.1](https://github.com/TeamLimRyan/TALES_OF_THE_WORLD_SUMMONERS_LINEAGE_KOREAN_LOCALIZATION_RELEASE/releases/tag/v1.0.1)에서 xdelta 패치를 받을 수 있습니다. 저장소 Git 이력과 릴리스에는 원본 ROM, 완성 ROM, BIOS, 세이브 데이터를 포함하지 않습니다.

- 패치 파일: `Tales_of_the_World_Summoners_Lineage_KO.xdelta`
- 패치 크기: `257,128 bytes`
- 패치 SHA-256: `673d921ab3c29b585d1b7e2ccf28a9fa8b1a29cfbbc1d6791187c97cd24c856f`

## 설치

Python 3과 `xdelta3`가 준비되어 있으면 저장소 루트에서 다음 명령으로 원본 확인, 패치 적용, 결과 검증을 한 번에 수행할 수 있습니다.

```powershell
python scripts/apply_patch.py "Tales of the World - Summoner's Lineage (Japan).gba"
```

직접 적용할 때는 다음 명령을 사용합니다.

```powershell
xdelta3 -d -s "Tales of the World - Summoner's Lineage (Japan).gba" `
  "Tales_of_the_World_Summoners_Lineage_KO.xdelta" `
  "summoners_lineage_ko.gba"
```

자세한 절차는 [설치 안내](INSTALL_KO.md), 지원 범위는 [호환성](COMPATIBILITY_KO.md)을 확인하십시오.

## 결과 무결성

정상 적용 결과는 다음과 같습니다.

- 결과 크기: `9,023,416 bytes`
- 결과 SHA-256: `ba353cfd547db33460711065cefec526920e39e4a09f2e3d4a3883c5ee36bc9e`

배포 xdelta를 대상 원본에 역적용한 결과가 최종 검수 ROM과 바이트 단위로 일치함을 확인했습니다. 전체 체크섬은 [SHA256SUMS.txt](SHA256SUMS.txt)에 있습니다.

## 오류 제보

[지원 안내](SUPPORT_KO.md)에 따라 원본 해시, 패치 해시, 출력 해시, 사용한 xdelta 버전과 에뮬레이터 정보를 Issues에 남겨 주십시오. ROM이나 세이브 파일은 첨부하지 마십시오.

## 배포 및 권리

이 프로젝트는 비공식 팬메이드 한국어 패치입니다. 게임, 상표, 로고와 원본 데이터의 권리는 각 권리자에게 있습니다. 이 저장소는 원본 게임을 제공하거나 대체하지 않으며, 사용자는 정당하게 보유한 대상 일본판 ROM을 직접 준비해야 합니다.
