# PyNmap Pro 🔍


Advanced Python-based Network Scanning Suite with Enhanced Features By `RkineX`⚡

## 🚀 Features
- **3x Faster Scanning** with async multi-threading
- **Smart Vulnerability Detection** with integrated CVE DB
- **Multiple Output Formats** (Text/JSON/XML)
- **Preset Scanning Modes** (Fast/Full/Stealth)
- **Real-time Visual Mapping**
- **Comprehensive Reporting**

## 📦 Installation
```bash
git clone https://github.com/yourusername/PyNmap-Pro.git
cd PyNmap-Pro
pip install -r requirements.txt
```

## 🛠 Usage
```bash
python -m src.cli.interface [TARGETS] [OPTIONS]

Basic Scan:
python -m src.cli.interface 192.168.1.1

Advanced Scan:
python -m src.cli.interface 10.0.0.0/24 -m full -p 1-65535 -v -o json
```

## 📌 Options
| Option | Description |
|--------|-------------|
| `-p`   | Port range (default: 1-1000) |
| `-m`   | Scan mode: fast/full/stealth |
| `-v`   | Enable vulnerability check |
| `-o`   | Output format: text/json/xml |

## 📊 Feature Comparison
| Feature                | Standard Nmap | PyNmap Pro |
|------------------------|---------------|------------|
| Parallel Scanning      | ❌            | ✅         |
| Vulnerability Analysis | Manual        | Auto       |
| Output Formats         | 6             | 3+         |
| Learning Curve         | Steep         | Easy       |
| Reporting              | Basic         | Advanced   |

## 📜 Legal Notice
⚠️ **Use Responsibly!** Unauthorized scanning is illegal. Always obtain proper authorization before scanning any network.

```bash
# Example Legal Scan
python -m src.cli.interface scanme.nmap.org -m fast
```

## 🛡 Security Features
- Encrypted report storage
- Audit logging
- Permission-based access control
- Data sanitization protocols

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License
MIT License - See [LICENSE](LICENSE) for details
