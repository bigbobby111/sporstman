<script setup>
import { ref, computed, onMounted } from "vue";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination, Autoplay } from "swiper/modules";
import { useHead } from "@unhead/vue";
import axios from "axios";
useHead({
  title: "СпортНовости",
  meta: [
    { name: "description", content: "Новости спорта" },
    {
      name: "keywords",
      content:
        "спорт, новости, спортивные события, футбол, баскетбол, хоккей, теннис, бокс, спортивные новости, матчи",
    },
  ],
});
const swiperModules = [Pagination, Autoplay];
const mobileMenuOpen = ref(false);
const currentCategory = ref("Все");
const news = ref();
const URL = "http://127.0.0.1:8000";

const toggleCategory = (category) => {
  currentCategory.value = category;
};
const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const fetchNews = async () => {
  try {
    const { data } = await axios.get(`${URL}/api/news/`);
    news.value = data;
    console.log(data);
  } catch (err) {
    console.log(err);
  } finally {
    console.log(news.value);
  }
};

const filteredNews = computed(() => {
  if (!news.value) return [];

  return news.value.filter((item) => {
    const isInCategory =
      currentCategory.value === "Все" ||
      item.category === currentCategory.value;
    return isInCategory && item.is_slider === false;
  });
});

const sliderNews = computed(() => {
  if (!news.value) return [];

  return news.value.filter((item) => item.is_slider === true);
});

const timeAgo = (dateStr) => {
  const date = new Date(dateStr);
  const now = new Date();
  const seconds = Math.floor((now - date) / 1000);

  const intervals = [
    { label: "год", seconds: 31536000 },
    { label: "месяц", seconds: 2592000 },
    { label: "день", seconds: 86400 },
    { label: "час", seconds: 3600 },
    { label: "минута", seconds: 60 },
  ];

  for (const interval of intervals) {
    const count = Math.floor(seconds / interval.seconds);
    if (count >= 1) {
      const plural =
        interval.label === "день"
          ? count === 1
            ? "день"
            : count < 5
            ? "дня"
            : "дней"
          : interval.label === "час"
          ? count === 1
            ? "час"
            : count < 5
            ? "часа"
            : "часов"
          : interval.label === "минута"
          ? count === 1
            ? "минута"
            : count < 5
            ? "минуты"
            : "минут"
          : interval.label === "месяц"
          ? count === 1
            ? "месяц"
            : count < 5
            ? "месяца"
            : "месяцев"
          : interval.label === "год"
          ? count === 1
            ? "год"
            : count < 5
            ? "года"
            : "лет"
          : interval.label;

      return `${count} ${plural} назад`;
    }
  }

  return "только что";
};

onMounted(() => {
  fetchNews();
});
</script>

<template>
  <!-- Header -->
  <header class="header">
    <div class="header-content">
      <!-- Logo -->
      <div class="logo">
        <a href="#" class="logo-link">
          <i class="fas fa-running"></i>
          <span>СпортНовости</span>
        </a>
      </div>
      <!-- Main Navigation -->
      <nav class="main-nav">
        <p
          @click="toggleCategory('Все')"
          :class="{ active: currentCategory === 'Все' }"
          class="nav-link"
        >
          Все виды
        </p>
        <p
          @click="toggleCategory('Футбол')"
          :class="{ active: currentCategory === 'Футбол' }"
          class="nav-link"
        >
          Футбол
        </p>
        <p
          @click="toggleCategory('Хоккей')"
          :class="{ active: currentCategory === 'Хоккей' }"
          class="nav-link"
        >
          Хоккей
        </p>
        <p
          @click="toggleCategory('Баскетбол')"
          :class="{ active: currentCategory === 'Баскетбол' }"
          class="nav-link"
        >
          Баскетбол
        </p>
        <p
          @click="toggleCategory('Теннис')"
          :class="{ active: currentCategory === 'Теннис' }"
          class="nav-link"
        >
          Теннис
        </p>
        <p
          @click="toggleCategory('Бокс')"
          :class="{ active: currentCategory === 'Бокс' }"
          class="nav-link"
        >
          Бокс
        </p>
      </nav>
      <!-- Mobile Menu Button -->
      <div class="menu-button">
        <button @click="toggleMobileMenu">
          <i class="fas fa-bars"></i>
        </button>
      </div>
    </div>
    <!-- Mobile Menu -->
    <div v-if="mobileMenuOpen" class="mobile-menu">
      <nav class="mobile-nav">
        <p @click="toggleCategory('Все')" class="mobile-nav-link">Все виды</p>
        <p @click="toggleCategory('Футбол')" class="mobile-nav-link">Футбол</p>
        <p @click="toggleCategory('Хоккей')" class="mobile-nav-link">Хоккей</p>
        <p @click="toggleCategory('Баскетбол')" class="mobile-nav-link">
          Баскетбол
        </p>
        <p @click="toggleCategory('Теннис')" class="mobile-nav-link">Теннис</p>
        <p @click="toggleCategory('Бокс')" class="mobile-nav-link">Бокс</p>
      </nav>
    </div>
  </header>
  <!-- Main Content -->
  <main class="main-content">
    <div class="hero-slider">
      <swiper
        :modules="swiperModules"
        :pagination="{ clickable: true }"
        :autoplay="{ delay: 5000, disableOnInteraction: false }"
        :slides-per-view="1"
      >
        <swiper-slide v-for="(slide, index) in sliderNews" :key="index">
          <div class="hero-slide">
            <img
              :src="slide.image"
              alt="Спортивная новость"
              class="hero-image"
            />
            <div class="hero-overlay">
              <div class="hero-text">
                <span class="category-badge">{{ slide.category }}</span>
                <h2 class="hero-title">{{ slide.title }}</h2>
                <p class="hero-description">{{ slide.description }}</p>
                <div class="hero-time">
                  <i class="far fa-clock"></i>
                  <span>{{ timeAgo(slide.time) }}</span>
                </div>
              </div>
            </div>
          </div>
        </swiper-slide>
      </swiper>
    </div>
    <div class="news-grid">
      <h2 class="section-title">Последние новости</h2>
      <div class="news-items">
        <div
          v-for="(news, index) in filteredNews"
          :key="index"
          class="news-item"
        >
          <div class="news-image">
            <img :src="news.image" alt="Спортивная новость" class="news-img" />
          </div>
          <div class="news-info">
            <div class="news-meta">
              <span class="category-badge">{{ news.category }}</span>
              <span class="news-time">
                <i class="far fa-clock"></i>
                {{ timeAgo(news.time) }}
              </span>
            </div>
            <h3 class="news-title">{{ news.title }}</h3>
            <p class="news-description">{{ news.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </main>
  <!-- Footer -->
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-left">
        <h3 class="footer-title">О нас</h3>
        <p class="footer-text">
          СпортНовости - ваш надежный источник спортивных новостей и аналитики с
          2010 года.
        </p>
      </div>
      <div class="footer-right">
        <h3 class="footer-title">Разделы</h3>
        <ul class="footer-list">
          <li>
            <p
              @click="toggleCategory('Все')"
              :class="{ active: currentCategory === 'Все' }"
              class="footer-link"
            >
              Все виды
            </p>
          </li>
          <li>
            <p
              @click="toggleCategory('Футбол')"
              :class="{ active: currentCategory === 'Футбол' }"
              class="footer-link"
            >
              Футбол
            </p>
          </li>
          <li>
            <p
              @click="toggleCategory('Хоккей')"
              :class="{ active: currentCategory === 'Хоккей' }"
              class="footer-link"
            >
              Хоккей
            </p>
          </li>
          <li>
            <p
              @click="toggleCategory('Баскетбол')"
              :class="{ active: currentCategory === 'Баскетбол' }"
              class="footer-link"
            >
              Баскетбол
            </p>
          </li>
          <li>
            <p
              @click="toggleCategory('Теннис')"
              :class="{ active: currentCategory === 'Теннис' }"
              class="footer-link"
            >
              Теннис
            </p>
          </li>
          <li>
            <p
              @click="toggleCategory('Бокс')"
              :class="{ active: currentCategory === 'Бокс' }"
              class="footer-link"
            >
              Бокс
            </p>
          </li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="footer-copy">© 2025 СпортНовости. Все права защищены.</p>
      <div class="footer-links">
        <a href="#" class="footer-link">Политика конфиденциальности</a>
        <a href="#" class="footer-link">Условия использования</a>
        <a href="#" class="footer-link">Карта сайта</a>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Header */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 50;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px;
  max-width: 1200px;
  margin: 0 auto;
}

.logo-link {
  font-size: 24px;
  font-weight: bold;
  color: #1e40af;
  display: flex;
  align-items: center;
}

.logo-link i {
  margin-right: 8px;
}

.main-nav {
  display: flex;
  gap: 24px;
}

.nav-link {
  color: #4b5563;
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
.nav-link.active {
  color: #1e40af;
}

.nav-link:hover {
  color: #1e40af;
  transition: all 0.3s ease-in-out;
}

.menu-button button {
  background: none;
  border: none;
  color: #4b5563;
  cursor: pointer;
  font-size: 20px;
}

.mobile-menu {
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.mobile-nav {
  display: flex;
  flex-direction: column;
  padding: 16px;
}

.mobile-nav-link {
  margin-bottom: 12px;
  color: #4b5563;
  text-decoration: none;
}

.mobile-nav-link:hover {
  color: #1e40af;
}

/* Main Content */
.main-content {
  padding-top: 96px;
  padding-bottom: 48px;
  padding-left: 16px;
  padding-right: 16px;
  max-width: 1200px;
  margin: 0 auto;
}

.hero-slider {
  margin-bottom: 40px;
}

.hero-slide {
  position: relative;
  height: 500px;
}

.hero-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0, 0, 0, 0.7), transparent);
  display: flex;
  align-items: flex-end;
  padding: 32px;
}

.hero-text {
  color: white;
}

.category-badge {
  background-color: #2563eb;
  color: white;
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 4px;
  margin-bottom: 16px;
  display: inline-block;
}

.hero-title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 16px;
}

.hero-description {
  color: #e5e7eb;
  margin-bottom: 16px;
}

.hero-time {
  display: flex;
  align-items: center;
}

.hero-time i {
  margin-right: 8px;
}

.hero-button {
  background-color: #2563eb;
  color: white;
  padding: 16px 32px;
  border-radius: 9999px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s;
}

.hero-button:hover {
  background-color: #1d4ed8;
}

/* News Grid */
.news-grid {
  margin-top: 32px;
}

.section-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
}

.news-items {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.news-item {
  background-color: white;
  border-radius: 8px;
  width: 367px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s;
}

.news-item:hover {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}
.news-image {
  width: 367px;
  height: 367px;
}
.news-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.news-info {
  padding: 16px;
}

.news-meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 16px;
}

.category-badge {
  background-color: #f3f4f6;
  color: #6b7280;
  font-size: 12px;
  padding: 4px 8px;
  border-radius: 4px;
}

.news-time {
  font-size: 12px;
  color: #9ca3af;
}

.news-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 12px;
}

.news-description {
  color: #6b7280;
  font-size: 14px;
}

/* Footer */
.footer {
  background-color: #1f2937;
  color: white;
  padding-top: 48px;
  padding-bottom: 24px;
}

.footer-content {
  display: flex;
  justify-content: space-evenly;
  margin-bottom: 32px;
}

.footer-left {
  max-width: 50%;
}

.footer-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.footer-text {
  color: #d1d5db;
}

.footer-right {
  max-width: 50%;
}

.footer-list {
  list-style: none;
}

.footer-link {
  color: #d1d5db;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}
.footer-link.active {
  color: #2563eb;
}

.footer-link:hover {
  color: #2563eb;
  transition: all 0.3s ease-in-out;
}

.footer-bottom {
  text-align: center;
  border-top: 1px solid #374151;
  padding-top: 16px;
}

.footer-copy {
  font-size: 14px;
  margin-bottom: 8px;
}

.footer-links {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.footer-links .footer-link {
  font-size: 14px;
}
</style>
