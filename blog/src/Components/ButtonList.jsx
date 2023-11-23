export const ButtonList = ({ categories, filterCategory }) => {
  return (
    <div className="categories">
      {categories.map((category) => (
        <button type="button" className="btn-category" key={category} onClick={() => filterCategory(category)}>
          {category}
        </button>
      ))}
    </div>
  );
};
