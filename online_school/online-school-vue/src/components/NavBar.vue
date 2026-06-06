<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container">
      <a class="navbar-brand">Online School</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <a class="nav-link">Уроки</a>
          </li>
          <li class="nav-item">
            <a class="nav-link">Создать урок</a>
          </li>
        </ul>
        <div class="d-flex align-items-center gap-2">
          <!-- <span class="text-body-secondary small">Вы вошли как {{ user.username }}</span> -->
          <form method="post" class="mb-0">
            <button type="submit" class="btn btn-outline-secondary btn-sm">Выйти</button>
          </form>
          <a class="btn btn-primary btn-sm">Войти</a>
        </div>
      </div>
    </div>
  </nav>
</template>
