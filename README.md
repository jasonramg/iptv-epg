<div align="center">

# 📺 IPTV EPG

### Automatically Updated XMLTV Electronic Program Guides

Reliable • Lightweight • XMLTV Compatible

![GitHub License](https://img.shields.io/github/license/jasonramg/iptv-epg?style=for-the-badge)
![GitHub Last Commit](https://img.shields.io/github/last-commit/jasonramg/iptv-epg?style=for-the-badge)
![GitHub Repo Size](https://img.shields.io/github/repo-size/jasonramg/iptv-epg?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/jasonramg/iptv-epg?style=for-the-badge)

XMLTV Electronic Program Guides for supported IPTV providers.

</div>

---

## 🚀 Quick Start

Use the appropriate XMLTV guide URL in your IPTV player.

| Provider | XMLTV | GZIP |
| :------- | :---- | :--- |
| RunNTV | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/runntv.xml` | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/runntv.xml.gz` |
| YuppTV | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml` | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/yupptv.xml.gz` |
| SunDirect GO | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/sundirectgo.xml` | `https://raw.githubusercontent.com/jasonramg/iptv-epg/main/epg/sundirectgo.xml.gz` |

---

## ✨ Features

- 📺 XMLTV compliant
- 🔄 Automatically updated
- 📦 Available in both `.xml` and `.xml.gz` formats
- ⚡ Lightweight and ready to use
- 📱 Compatible with most IPTV players
- 🌏 Easily expandable with additional providers

---

## 📡 Available Providers

| Provider | XML | XML.GZ | Status |
| :------- | :-- | :----- | :----: |
| RunNTV | ✅ | ✅ | 🟢 |
| YuppTV | ✅ | ✅ | 🟢 |
| SunDirect GO | ✅ | ✅ | 🟢 |

More providers will be added over time.

---

## 📱 Compatible Applications

These guides work with any application supporting the XMLTV format, including:

- IPTV Smarters
- TiviMate
- OTT Navigator
- Sparkle TV
- Kodi
- VLC
- Jellyfin
- Emby
- Plex

---

## 📁 Repository Structure

```text
epg/
├── runntv.xml
├── runntv.xml.gz
├── yupptv.xml
├── yupptv.xml.gz
├── sundirectgo.xml
└── sundirectgo.xml.gz
```

---

## 📋 Guide Information

Depending on the provider, each guide may include:

- Programme titles
- Programme descriptions
- Categories
- Start and end times
- Episode information
- Languages
- Channel icons (where available)

---

## ❓ FAQ

### What is XMLTV?

XMLTV is a standard XML-based format used by IPTV players and media servers to display Electronic Program Guide (EPG) information.

### Should I use the `.xml` or `.xml.gz` file?

Both contain the same guide data.

- Use **`.xml.gz`** if your application supports compressed guides (recommended).
- Use **`.xml`** if your application does not support GZIP-compressed files.

### Does this repository include IPTV playlists?

No. This repository only provides XMLTV EPG metadata.

### Does this repository provide live TV streams?

No.

---

## ⚠️ Disclaimer

This repository distributes **Electronic Program Guide (EPG) metadata only**.

It does **not** host, distribute, or provide:

- IPTV playlists
- Live TV streams
- DRM keys
- Video or audio content
- Subscription services

Users are responsible for ensuring they have the necessary rights or subscriptions required to access television content through their chosen IPTV provider.

---

## 🤝 Contributing

Suggestions, bug reports, and pull requests are welcome.

If you'd like to request support for another IPTV provider, feel free to open an issue.

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

⭐ If you find this project useful, consider giving it a star.

Made with ❤️ by <strong>JasonRamG</strong>

</div>
