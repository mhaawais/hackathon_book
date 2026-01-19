"""
Tests for metadata validation logic
"""
import unittest
from backend.retrieval_validator import RetrievalValidator, RetrievedChunk, MetadataVerification


class TestMetadataValidation(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Note: This test will require actual API keys to run properly
        # For unit testing purposes, we'll test the structure and validation logic
        pass

    def test_verify_metadata_complete(self):
        """Test metadata verification with complete data."""
        validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

        chunk = RetrievedChunk(
            score=0.8,
            url="https://example.com/docs/intro",
            heading="Introduction",
            chunk_index=0,
            chunk_text="This is a sample content chunk.",
            section="Getting Started",
            validation_passed=False
        )

        result = validator._verify_metadata(chunk)

        # All fields should be valid, so overall score should be 1.0
        self.assertIsInstance(result, MetadataVerification)
        self.assertTrue(result.url_valid)
        self.assertTrue(result.heading_present)
        self.assertTrue(result.section_correct)
        self.assertTrue(result.chunk_index_valid)
        self.assertTrue(result.text_quality)
        self.assertEqual(result.overall_score, 1.0)

    def test_verify_metadata_missing_fields(self):
        """Test metadata verification with missing fields."""
        validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

        # Test with missing heading and section
        chunk = RetrievedChunk(
            score=0.8,
            url="https://example.com/docs/intro",
            heading="",  # Missing
            chunk_index=0,
            chunk_text="This is a sample content chunk.",
            section="",  # Missing
            validation_passed=False
        )

        result = validator._verify_metadata(chunk)

        self.assertIsInstance(result, MetadataVerification)
        self.assertTrue(result.url_valid)
        self.assertFalse(result.heading_present)
        self.assertFalse(result.section_correct)
        self.assertTrue(result.chunk_index_valid)
        self.assertTrue(result.text_quality)
        # 3 out of 5 fields are valid = 60% score
        self.assertAlmostEqual(result.overall_score, 0.6, places=1)

    def test_verify_metadata_invalid_url(self):
        """Test metadata verification with invalid URL."""
        validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

        # Test with invalid URL
        chunk = RetrievedChunk(
            score=0.8,
            url="",  # Invalid
            heading="Introduction",
            chunk_index=0,
            chunk_text="This is a sample content chunk.",
            section="Getting Started",
            validation_passed=False
        )

        result = validator._verify_metadata(chunk)

        self.assertIsInstance(result, MetadataVerification)
        self.assertFalse(result.url_valid)
        self.assertTrue(result.heading_present)
        self.assertTrue(result.section_correct)
        self.assertTrue(result.chunk_index_valid)
        self.assertTrue(result.text_quality)
        # 4 out of 5 fields are valid = 80% score
        self.assertAlmostEqual(result.overall_score, 0.8, places=1)

    def test_verify_metadata_empty_text(self):
        """Test metadata verification with empty text."""
        validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

        # Test with empty text
        chunk = RetrievedChunk(
            score=0.8,
            url="https://example.com/docs/intro",
            heading="Introduction",
            chunk_index=0,
            chunk_text="",  # Empty
            section="Getting Started",
            validation_passed=False
        )

        result = validator._verify_metadata(chunk)

        self.assertIsInstance(result, MetadataVerification)
        self.assertTrue(result.url_valid)
        self.assertTrue(result.heading_present)
        self.assertTrue(result.section_correct)
        self.assertTrue(result.chunk_index_valid)
        self.assertFalse(result.text_quality)
        # 4 out of 5 fields are valid = 80% score
        self.assertAlmostEqual(result.overall_score, 0.8, places=1)

    def test_validate_metadata_integrity(self):
        """Test overall metadata integrity validation."""
        validator = RetrievalValidator.__new__(RetrievalValidator)  # Create without init

        chunks = [
            RetrievedChunk(
                score=0.8,
                url="https://example.com/docs/intro",
                heading="Introduction",
                chunk_index=0,
                chunk_text="This is a sample content chunk.",
                section="Getting Started",
                validation_passed=False
            ),
            RetrievedChunk(
                score=0.7,
                url="https://example.com/docs/chapter1",
                heading="Chapter 1",
                chunk_index=1,
                chunk_text="More content here.",
                section="Main Content",
                validation_passed=False
            )
        ]

        result = validator.validate_metadata_integrity(chunks)

        self.assertIsInstance(result, MetadataVerification)
        # With 2 valid chunks, all metrics should pass (>80% threshold)
        self.assertTrue(result.url_valid)
        self.assertTrue(result.heading_present)
        self.assertTrue(result.section_correct)
        self.assertTrue(result.chunk_index_valid)
        self.assertTrue(result.text_quality)


if __name__ == '__main__':
    unittest.main()