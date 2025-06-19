<template>
  <div class="container py-5">
       <h2 class="mb-4"> Customer Feedback Tracker</h2>
       <ReplyCounter />
       <ThemeToggle />
  </div>
</template>


<script>
 import ReplyCounter from './components/ReplyCounter.vue';
 import ThemeToggle from './components/ThemeToggle.vue';
 
 export default {
  components: {
    ReplyCounter,
    ThemeToggle
  }
 };
</script>

<!-- <template>
  <ReplyCounter />
</template>


<script>
  import ReplyCounter from './components/ReplyCounter.vue'

  export default {
    components: {
      ReplyCounter
    }
  }
</script> -->