<template>
    <div class="card p-3 shadow-sm">
         <h5>Theme Toggle</h5>
         <button :class="buttonClass" @click="toggleTheme">
             Change Theme
         </button>
    </div>

</template>

<script>
  export default {
    name: 'ThemeToggle',
    data() {
        return {
            isPrimary: true
        };
    },
    computed: {
        buttonClass() {
            return this.isPrimary ? 'btn btn-primary' : 'btn btn-success';
        }
    },
    methods: {
        toggleTheme() {
            this.isPrimary = !this.isPrimary;
        }
    }
  };
</script>