# Visual Enhancer 1.21.50 (Resource Pack)

Готовый **resource pack only** для Bedrock 1.21.50, совместимый с серверами/Realms,
потому что не содержит behavior pack, скриптов и модов.

## Важно про PR и бинарные файлы

В этом репозитории PNG-файлы **не хранятся** (чтобы системы PR, где запрещены binary diff,
работали стабильно). Перед упаковкой пакета сгенерируй ассеты локально:

```bash
python scripts/generate_visual_pack_assets.py
```

## Что включено

- Entity ESP через яркие override-текстуры сущностей.
- Chest ESP через цветовые текстуры для chest / trapped chest / ender chest / barrel / shulker.
- Target ESP визуальным overlay-стилем (texture-based accent).
- Дополнительные визуальные улучшения:
  - более прозрачный fire overlay,
  - clear-water стиль,
  - яркие ore-текстуры (без wallhack),
  - варианты прицела.
- Кастомный экран Visual Settings в UI и кнопка в pause menu.

## Важное ограничение Bedrock RP

JSON UI внутри resource pack не может полноценно менять игровые рендер-параметры на лету
как мод-меню. Поэтому переключатели/слайдеры в этом паке — UI-слой для пресетов.
Сами визуальные изменения применяются как активный ресурс-пак.

## Установка

1. Выполни `python scripts/generate_visual_pack_assets.py`.
2. Сожми папку `resource_packs/VisualEnhancer2150` в zip.
3. Переименуй в `.mcpack`.
4. Открой файл через Minecraft Bedrock.
5. Активируй в Global Resources.
