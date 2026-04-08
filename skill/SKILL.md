---
name: thumbnail-cli
description: "Invoke this skill to run the thumbnail-cli tool and generate 1280×670px thumbnail images for note.com articles and blog posts. You MUST use this skill whenever the user asks to create a thumbnail (サムネイル), サムネ, header image, OGP image, or article cover image — even casually phrased as 「サムネイル作って」「note記事の画像が欲しい」or 'make a thumbnail for my post about X'. This skill is essential because it knows the exact tool path, the full list of available templates (default, dark, gradient, gradient-sunset, gradient-ocean, gradient-forest, gradient-rose, gradient-sakura), CLI flags (--subtitle, --author, --font-weight, --output), and the template-selection logic that maps content type to the best visual style. Without this skill you cannot correctly invoke the tool."
---

# thumbnail-cli

Generate 1280×670px thumbnail images for note.com posts (and future platforms) with multiple templates to match the mood of any article.

## Tool

```bash
python3 /home/ss160341/_work/thumbnail-cli/thumbnail.py \
  --title "タイトル" \
  [--subtitle "サブタイトル"] \
  [--author "著者名"] \
  [--template <name>] \
  [--font-weight <100-900>] \
  [--output <filename.png>]
```

## Options

| Option | Description | Default |
|---|---|---|
| `--title` | Main title text (required) | — |
| `--subtitle` | Subtitle text | none |
| `--author` | Author name, shown bottom-left | none |
| `--template` | Template name (see below) | `default` |
| `--font-weight` | 100=Thin, 400=Regular, 700=Bold, 900=Black | `700` |
| `--output` | Output filename | `thumbnail-{title}.png` |

## Templates

| Template | Colors | Best for |
|---|---|---|
| `default` | White background, dark text | Neutral, professional, minimal, informational |
| `dark` | Black background, white text | Tech, programming, engineering, night theme |
| `gradient` | Purple → Blue | General creative, broad or lifestyle topics |
| `gradient-sunset` | Orange → Hot Pink | Warm, personal stories, lifestyle, experience posts |
| `gradient-ocean` | Teal → Navy | Calm, educational, business, study |
| `gradient-forest` | Dark Green → Lime | Nature, wellness, health, environment |
| `gradient-rose` | Deep Purple → Coral Pink | Beauty, fashion, romance, creative writing |
| `gradient-sakura` | Cherry Pink → Pale Pink | Japanese culture, spring, soft or delicate topics |

## Selecting a template

**If the user specifies a template** — use it exactly as requested.

**If the user doesn't specify** — infer from the title and content using these signals:

- Technical content: "プログラミング", "エンジニア", "コード", "Python", "API", "開発", "技術" → `dark`
- Sakura/spring/soft: "春", "桜", "さくら", "やさしい", "ふんわり" → `gradient-sakura`
- Nature/health: "自然", "環境", "健康", "ウェルネス", "食", "植物" → `gradient-forest`
- Warm personal stories: "体験談", "日記", "副業", "お金", "暮らし", "ライフスタイル" → `gradient-sunset`
- Business/study/education: "ビジネス", "勉強", "学習", "資格", "仕事術" → `gradient-ocean`
- Beauty/fashion/romance: "美容", "ファッション", "恋愛", "コーデ" → `gradient-rose`
- Creative, broad topics → `gradient`
- Neutral, undecided, informational → `default`

When you auto-select, briefly explain your reasoning after generating the image.

## After generating

Report:
1. The output file path
2. The image dimensions (1280×670px)
3. Which template was used
4. Why you chose it (if auto-selected)
