<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bảng Tuần Hoàn Các Nguyên Tố Hóa Học - Thông Minh</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        kimloai: '#f59e0b',
                        kimloaichuyentiep: '#ef4444',
                        kimloaiamd: '#3b82f6',
                        kimloaitrunggian: '#10b981',
                        phikim: '#8b5cf6',
                        khiphantinh: '#06b6d4',
                        kimoithi: '#ec4899',
                        lanthan: '#f97316',
                        actini: '#d946ef',
                    },
                },
            }
        }
    </script>
    <style type="text/tailwindcss">
        @layer utilities {
            .element-cell {
                @apply w-16 h-16 m-0.5 rounded-md flex flex-col items-center justify-center cursor-pointer transition-all duration-200 border-2 border-transparent;
            }
            .element-cell:hover {
                @apply scale-110 shadow-lg border-white;
            }
            .element-active {
                @apply ring-4 ring-white scale-105;
            }
            .electron-shell {
                @apply absolute rounded-full border-2 border-sky-400/70 flex items-center justify-center;
            }
            .electron {
                @apply w-3 h-3 bg-yellow-400 rounded-full absolute;
            }
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white min-h-screen">
    <header class="container mx-auto py-4 px-4 text-center">
        <h1 class="text-[clamp(1.5rem,4vw,2.5rem)] font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 to-purple-500">
            BẢNG TUẦN HOÀN CÁC NGUYÊN TỐ HÓA HỌC
        </h1>
        <p class="text-gray-300 mt-2">Nhấp vào một nguyên tố để xem thông tin chi tiết, cấu trúc và mô phỏng phản ứng</p>
    </header>

    <!-- Bảng Tuần Hoàn -->
    <main class="container mx-auto px-2 pb-8">
        <div class="overflow-x-auto pb-4">
            <div id="periodic-table" class="min-w-[900px] mx-auto">
                <!-- Bảng sẽ được tạo động bằng JavaScript -->
            </div>
        </div>

        <!-- Chú thích -->
        <div class="mt-4 flex flex-wrap gap-3 justify-center text-sm">
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-kimloai"></span> Kim loại kiềm</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-kimloaichuyentiep"></span> Kim loại chuyển tiếp</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-kimloaiamd"></span> Kim loại am đất</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-kimloaitrunggian"></span> Kim loại trung gian</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-phikim"></span> Phi kim</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-khiphantinh"></span> Khí hiếm</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-kimoithi"></span> Kim loại thi</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-lanthan"></span> Lantan</div>
            <div class="flex items-center gap-2"><span class="w-4 h-4 rounded bg-actini"></span> Actini</div>
        </div>

        <!-- Thông tin chi tiết & Mô phỏng -->
        <div id="info-panel" class="mt-8 bg-slate-800/60 rounded-2xl p-6 backdrop-blur-md hidden">
            <div class="grid md:grid-cols-2 gap-6">
                <!-- Thông tin cơ bản -->
                <div>
                    <div class="flex items-center gap-4 mb-4">
                        <div id="element-symbol" class="w-24 h-24 rounded-xl flex flex-col items-center justify-center text-3xl font-bold"></div>
                        <div>
                            <h2 id="element-name" class="text-2xl font-bold"></h2>
                            <p id="element-vn-name" class="text-gray-300"></p>
                            <p id="element-number" class="text-sm text-gray-400"></p>
                        </div>
                    </div>
                    
                    <div class="space-y-2 text-sm">
                        <div class="flex justify-between border-b border-gray-700 pb-1">
                            <span class="text-gray-400">Khối lượng nguyên tử:</span>
                            <span id="element-mass"></span>
                        </div>
                        <div class="flex justify-between border-b border-gray-700 pb-1">
                            <span class="text-gray-400">Cấu hình điện tử:</span>
                            <span id="element-config"></span>
                        </div>
                        <div class="flex justify-between border-b border-gray-700 pb-1">
                            <span class="text-gray-400">Nhóm, Chu kỳ:</span>
                            <span id="element-group-period"></span>
                        </div>
                        <div class="flex justify-between border-b border-gray-700 pb-1">
                            <span class="text-gray-400">Trạng thái ở 25°C:</span>
                            <span id="element-state"></span>
                        </div>
                        <div class="flex justify-between border-b border-gray-700 pb-1">
                            <span class="text-gray-400">Độ âm điện:</span>
                            <span id="element-electronegativity"></span>
                        </div>
                        <div class="mt-3">
                            <h3 class="font-semibold text-cyan-400 mb-1">Mô tả:</h3>
                            <p id="element-description" class="text-gray-300 text-sm leading-relaxed"></p>
                        </div>
                    </div>
                </div>

                <!-- Mô phỏng nguyên tử và phản ứng -->
                <div>
                    <h3 class="font-bold text-lg mb-3 text-center text-yellow-400">Cấu trúc nguyên tử</h3>
                    <div id="atom-model" class="relative w-full h-64 flex items-center justify-center bg-slate-900/50 rounded-xl mb-6 overflow-hidden">
                        <div id="nucleus" class="w-10 h-10 bg-red-500 rounded-full flex items-center justify-center text-xs font-bold z-10"></div>
                        <!-- Lớp vỏ điện tử sẽ được tạo động -->
                    </div>

                    <h3 class="font-bold text-lg mb-3 text-center text-green-400">Mô phỏng phản ứng hóa học</h3>
                    <div class="bg-slate-900/50 rounded-xl p-4">
                        <div class="flex gap-2 mb-3">
                            <select id="reactant-select" class="flex-1 bg-slate-700 rounded px-2 py-1.5 text-sm">
                                <option value="">Chọn nguyên tố kết hợp...</option>
                            </select>
                            <button id="react-btn" class="bg-green-600 hover:bg-green-500 px-3 py-1.5 rounded text-sm transition-colors">
                                <i class="fa fa-flask"></i> Phản ứng
                            </button>
                        </div>
                        <div id="reaction-result" class="min-h-[80px] p-3 bg-slate-800 rounded text-sm">
                            Chọn nguyên tố khác để xem các phản ứng có thể xảy ra.
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <footer class="text-center py-4 text-gray-400 text-sm">
        <p>Nguồn dữ liệu: Dữ liệu hóa học chuẩn | Thiết kế cho giáo dục & học tập</p>
    </footer>

    <script>
        // Dữ liệu các nguyên tố chính
        const elements = [
            { z: 1, symbol: "H", name: "Hydro", vnName: "Hiđro", mass: "1.008", category: "phikim", group: 1, period: 1, config: "1s¹", state: "Khí", electronegativity: 2.2, valence: 1, description: "Nguyên tố nhẹ nhất, phổ biến nhất vũ trụ, dễ cháy trong không khí." },
            { z: 2, symbol: "He", name: "Helium", vnName: "Heli", mass: "4.0026", category: "khiphantinh", group: 18, period: 1, config: "1s²", state: "Khí", electronegativity: null, valence: 0, description: "Khí hiếm, không màu, không mùi, khó hóa hợp, dùng trong bóng bay." },
            { z: 3, symbol: "Li", name: "Lithium", vnName: "Liti", mass: "6.94", category: "kimloai", group: 1, period: 2, config: "[He] 2s¹", state: "Rắn", electronegativity: 0.98, valence: 1, description: "Kim loại kiềm nhẹ nhất, dùng trong pin, dễ phản ứng với nước." },
            { z: 4, symbol: "Be", name: "Beryllium", vnName: "Beri", mass: "9.0122", category: "kimloaiamd", group: 2, period: 2, config: "[He] 2s²", state: "Rắn", electronegativity: 1.57, valence: 2, description: "Kim loại nhẹ, cứng, độc, dùng trong chế tạo hợp kim nhẹ." },
            { z: 5, symbol: "B", name: "Boron", vnName: "Bo", mass: "10.81", category: "kimoithi", group: 13, period: 2, config: "[He] 2s²2p¹", state: "Rắn", electronegativity: 2.04, valence: 3, description: "Nguyên tố bán kim loại, dùng trong thủy tinh, thuốc trừ sâu." },
            { z: 6, symbol: "C", name: "Carbon", vnName: "Cacbon", mass: "12.011", category: "phikim", group: 14, period: 2, config: "[He] 2s²2p²", state: "Rắn", electronegativity: 2.55, valence: 4, description: "Nền tảng của hóa học hữu cơ, tồn tại dưới dạng kim cương, than chì." },
            { z: 7, symbol: "N", name: "Nitrogen", vnName: "Nitơ", mass: "14.007", category: "phikim", group: 15, period: 2, config: "[He] 2s²2p³", state: "Khí", electronegativity: 3.04, valence: 3, description: "Chiếm 78% không khí, rất quan trọng cho sinh vật, phân bón." },
            { z: 8, symbol: "O", name: "Oxygen", vnName: "Oxi", mass: "15.999", category: "phikim", group: 16, period: 2, config: "[He] 2s²2p⁴", state: "Khí", electronegativity: 3.44, valence: 2, description: "Khí cần thiết cho hô hấp, đốt cháy, chiếm 21% không khí." },
            { z: 9, symbol: "F", name: "Fluorine", vnName: "Flo", mass: "18.998", category: "phikim", group: 17, period: 2, config: "[He] 2s²2p⁵", state: "Khí", electronegativity: 3.98, valence: 1, description: "Phi kim mạnh nhất, dễ phản ứng, dùng trong kem đánh răng." },
            { z: 10, symbol: "Ne", name: "Neon", vnName: "Neon", mass: "20.180", category: "khiphantinh", group: 18, period: 2, config: "[He] 2s²2p⁶", state: "Khí", electronegativity: null, valence: 0, description: "Khí hiếm, phát sáng khi có dòng điện, dùng trong đèn quảng cáo." },
            { z: 11, symbol: "Na", name: "Sodium", vnName: "Natri", mass: "22.990", category: "kimloai", group: 1, period: 3, config: "[Ne] 3s¹", state: "Rắn", electronegativity: 0.93, valence: 1, description: "Kim loại kiềm, phản ứng mạnh với nước, có trong muối ăn (NaCl)." },
            { z: 12, symbol: "Mg", name: "Magnesium", vnName: "Magie", mass: "24.305", category: "kimloaiamd", group: 2, period: 3, config: "[Ne] 3s²", state: "Rắn", electronegativity: 1.31, valence: 2, description: "Kim loại nhẹ, cháy sáng mạnh, cần thiết cho cơ thể con người." },
            { z: 13, symbol: "Al", name: "Aluminium", vnName: "Nhôm", mass: "26.982", category: "kimloaitrunggian", group: 13, period: 3, config: "[Ne] 3s²3p¹", state: "Rắn", electronegativity: 1.61, valence: 3, description: "Kim loại phổ biến, nhẹ, bền, dùng trong xây dựng, đồ dùng gia đình." },
            { z: 14, symbol: "Si", name: "Silicon", vnName: "Silic", mass: "28.085", category: "kimoithi", group: 14, period: 3, config: "[Ne] 3s²3p²", state: "Rắn", electronegativity: 1.90, valence: 4, description: "Nguyên tố chính của vi mạch điện tử, chiếm nhiều trong vỏ Trái Đất." },
            { z: 15, symbol: "P", name: "Phosphorus", vnName: "Phốt pho", mass: "30.974", category: "phikim", group: 15, period: 3, config: "[Ne] 3s²3p³", state: "Rắn", electronegativity: 2.19, valence: 3,5, description: "Quan trọng cho xương, răng, phân bón, dễ cháy trong không khí." },
            { z: 16, symbol: "S", name: "Sulfur", vnName: "Lưu huỳnh", mass: "32.06", category: "phikim", group: 16, period: 3, config: "[Ne] 3s²3p⁴", state: "Rắn", electronegativity: 2.58, valence: 2,4,6, description: "Chất rắn màu vàng, có trong núi lửa, làm thuốc trừ sâu, axit sulfuric." },
            { z: 17, symbol: "Cl", name: "Chlorine", vnName: "Clo", mass: "35.45", category: "phikim", group: 17, period: 3, config: "[Ne] 3s²3p⁵", state: "Khí", electronegativity: 3.16, valence: 1, description: "Khí màu xanh lá, độc, dùng khử trùng nước, làm muối ăn." },
            { z: 18, symbol: "Ar", name: "Argon", vnName: "Agon", mass: "39.948", category: "khiphantinh", group: 18, period: 3, config: "[Ne] 3s²3p⁶", state: "Khí", electronegativity: null, valence: 0, description: "Khí hiếm, chiếm 1% không khí, dùng trong bóng đèn." },
            { z: 19, symbol: "K", name: "Potassium", vnName: "Kali", mass: "39.098", category: "kimloai", group: 1, period: 4, config: "[Ar] 4s¹", state: "Rắn", electronegativity: 0.82, valence: 1, description: "Kim loại kiềm, cần thiết cho thực vật, có trong phân bón." },
            { z: 20, symbol: "Ca", name: "Calcium", vnName: "Canxi", mass: "40.078", category: "kimloaiamd", group: 2, period: 4, config: "[Ar] 4s²", state: "Rắn", electronegativity: 1.00, valence: 2, description: "Cần thiết cho xương, răng, vỏ trứng, xi măng." },
            { z: 26, symbol: "Fe", name: "Iron", vnName: "Sắt", mass: "55.845", category: "kimloaichuyentiep", group: 8, period: 4, config: "[Ar] 3d⁶4s²", state: "Rắn", electronegativity: 1.83, valence: 2,3, description: "Kim loại phổ biến nhất, chính của thép, có trong máu người." },
            { z: 29, symbol: "Cu", name: "Copper", vnName: "Đồng", mass: "63.546", category: "kimloaichuyentiep", group: 11, period: 4, config: "[Ar] 3d¹⁰4s¹", state: "Rắn", electronegativity: 1.90, valence: 1,2, description: "Dẫn điện tốt, màu đỏ đồng, dùng dây điện, tiền xu." },
            { z: 30, symbol: "Zn", name: "Zinc", vnName: "Kẽm", mass: "65.38", category: "kimloaichuyentiep", group: 12, period: 4, config: "[Ar] 3d¹⁰4s²", state: "Rắn", electronegativity: 1.65, valence: 2, description: "Dùng mạ chống gỉ, hợp kim đồng-kẽm là đồng thau." },
            { z: 47, symbol: "Ag", name: "Silver", vnName: "Bạc", mass: "107.87", category: "kimloaichuyentiep", group: 1