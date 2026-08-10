# 패치 형식

- 형식: VCDIFF/xdelta3
- 생성기: xdelta3 3.0.11
- 애플리케이션 헤더: 비활성화 (`-A`)
- 원본 ROM 포함: 아니요
- 완성 ROM 포함: 아니요

생성 명령:

```text
xdelta3 -f -e -A -s SOURCE.gba TARGET.gba PATCH.xdelta
```

검증 명령:

```text
xdelta3 -f -d -s SOURCE.gba PATCH.xdelta ROUNDTRIP.gba
```

`ROUNDTRIP.gba`의 SHA-256이 최종 검수 ROM의 SHA-256과 정확히 일치해야 합니다.
