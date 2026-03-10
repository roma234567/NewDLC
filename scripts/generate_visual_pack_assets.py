#!/usr/bin/env python3
"""Generate PNG assets for VisualEnhancer2150 pack.
Keeps repository text-only to avoid binary-file PR limitations.
"""
from pathlib import Path
import struct
import zlib

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "resource_packs" / "VisualEnhancer2150"


def write_png(path: Path, w: int, h: int, rgba: tuple[int, int, int, int]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sig = b"\x89PNG\r\n\x1a\n"

    def chunk(t: bytes, d: bytes) -> bytes:
        return (
            struct.pack("!I", len(d))
            + t
            + d
            + struct.pack("!I", zlib.crc32(t + d) & 0xFFFFFFFF)
        )

    row = bytes(rgba) * w
    raw = b"".join(b"\x00" + row for _ in range(h))
    ihdr = struct.pack("!IIBBBBB", w, h, 8, 6, 0, 0, 0)
    path.write_bytes(sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


FILES_16 = {
    "textures/ui/visual_settings_icon.png": (255, 215, 0, 255),
    "textures/ui/crosshair_default_plus.png": (255, 255, 255, 255),
    "textures/ui/crosshair_dot.png": (0, 255, 255, 255),
    "textures/ui/crosshair_thin.png": (180, 255, 180, 255),
    "textures/entity/zombie_esp.png": (0, 255, 0, 220),
    "textures/entity/skeleton_esp.png": (255, 255, 180, 220),
    "textures/entity/creeper_esp.png": (0, 255, 120, 220),
    "textures/entity/player_esp.png": (80, 180, 255, 220),
    "textures/entity/target_outline.png": (255, 64, 64, 180),
    "textures/entity/hitbox_overlay.png": (255, 0, 255, 90),
    "textures/blocks/chest_normal_highlight.png": (255, 170, 0, 255),
    "textures/blocks/chest_trapped_highlight.png": (255, 64, 64, 255),
    "textures/blocks/ender_chest_highlight.png": (180, 0, 255, 255),
    "textures/blocks/barrel_highlight.png": (64, 200, 255, 255),
    "textures/blocks/shulker_highlight.png": (255, 105, 180, 255),
    "textures/environment/fire_0_transparent.png": (255, 80, 0, 80),
    "textures/environment/fire_1_transparent.png": (255, 180, 0, 70),
    "textures/environment/water_clear.png": (40, 120, 255, 80),
    "textures/environment/skybox_day_animated_0.png": (70, 130, 255, 255),
    "textures/environment/skybox_day_animated_1.png": (120, 170, 255, 255),
    "textures/environment/ore_overlay_bright.png": (255, 255, 255, 180),
}


def main() -> None:
    for rel, color in FILES_16.items():
        write_png(PACK / rel, 16, 16, color)
    write_png(PACK / "pack_icon.png", 64, 64, (80, 120, 255, 255))
    print("Generated", len(FILES_16) + 1, "PNG assets in", PACK)


if __name__ == "__main__":
    main()
